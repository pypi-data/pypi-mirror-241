import asyncio
import time
from typing import Any, Dict

import requests
from threading import Thread
from .identity import DryId


class DryJob:
    def __init__(self, job_id, request):
        self.id = job_id
        self.request = request


class RunConfig:
    # Assuming this is a simplified representation of RunConfig from your Rust code
    def __init__(self, auth: Dict[str, Any] = {}, inject: Dict[str, str] = {}, disable_secrets: bool = False,
                 swap: Dict[DryId, Dict[str, Any]] = {}):
        self.auth = auth
        self.inject = inject
        self.disable_secrets = disable_secrets
        self.swap = swap

    def to_json(self):
        # Convert DryId instances to strings in the swap dictionary
        swap_str = {str(k): v for k, v in self.swap.items()}

        return {
            "auth": self.auth,
            "inject": self.inject,
            "disable_secrets": self.disable_secrets,
            "swap": swap_str
        }


class DryJobError:
    def __init__(self, status_code: int, description=""):
        if status_code < 400 or status_code > 599:
            raise ValueError("status_code must be between 400 and 599")
        self.status_code = status_code
        self.description = description

    def to_json(self):
        return {
            "status_code": self.status_code,
            "description": self.description,
            "timed_out": False
        }


class DryClient:
    def __init__(self, api_key, engine_host: str = "https://api.drymerge.com",
                 proxy_host="https://proxy-srv.drymerge.com",
                 proxy_name=DryId("worker", "queue"),
                 verbose=False):
        self.engine_host = engine_host
        self.proxy_identity = proxy_name
        self.proxy_host = proxy_host
        self.execute_endpoint = "/execute"
        self.hydrate_endpoint = "/upsert-with-template"
        self.delete_endpoint = "/remove-entities"
        self.register_proxy_endpoint = "/hire/*proxy_identity"
        self.submit_job_proxy_endpoint = "/retire/*job_id"
        self.get_jobs_proxy_endpoint = "/employ/*proxy_identity"
        self.api_key = api_key
        self.verbose = verbose
        self.handlers = {}  # Dictionary to map URLs to handler functions

    def run(self, dry_id: DryId, run_config: RunConfig = RunConfig(), args: Dict[str, Any] = {}) -> Dict[str, Any]:
        endpoint = f"{self.engine_host}{self.execute_endpoint}/{str(dry_id)}"  # Replace with your actual endpoint
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Construct the payload based on your Rust code structure
        payload = {
            "config": run_config,
            "args": args
        }
        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                self.report(f"Failed to run job with error: {response.json()['pretty_err']}")
                response.raise_for_status()  # This will raise an HTTPError with the status code and message
        except Exception as e:
            self.report(f"Failed to run job with error: {e}")
            raise e

    def template(self, dry_id: DryId, source: Dict[str, Any] = {}):
        endpoint = f"{self.engine_host}{self.hydrate_endpoint}"  # Replace with your actual endpoint
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "template": str(dry_id),
            "hydrate": source  # This is the source data you want to hydrate
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            if response.status_code == 200 or response.status_code == 201:
                self.report(f"Successfully hydrated template {dry_id}")
                return response
            else:
                self.report(f"Failed to run job with error: {response.text}")
                response.raise_for_status()  # This will raise an HTTPError with the status code and message
        except Exception as e:
            self.report(f"Failed to run job with error: {e}")
            raise e

    def delete(self, ids):
        endpoint = f"{self.engine_host}{self.delete_endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "entities": list(map(str, ids)),
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            if response.status_code == 200 or response.status_code == 201:
                self.report(f"Successfully deleted ids template {ids}")
                return response
            else:
                self.report(f"Failed to run job with error: {response.text}")
                response.raise_for_status()  # This will raise an HTTPError with the status code and message
        except Exception as e:
            self.report(f"Failed to run job with error: {e}")
            raise e

    def route(self, url, handler_function):
        """
        A handler function must accept a single dictionary argument, which will contain the request body and headers
        of the job.
        """
        self.handlers[url] = handler_function
        return self  # Allow chaining

    def register_proxy(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        proxy_identity = str(self.proxy_identity)
        url = f"{self.proxy_host}{self.register_proxy_endpoint.replace('*proxy_identity', proxy_identity)}"
        try:
            response = requests.post(url, headers=headers, json={"identity": proxy_identity})
            if response.status_code == 200 or response.status_code == 201:
                self.report(f"Successfully registered proxy {proxy_identity}")
            else:
                print(f"Failed to register proxy {proxy_identity} with error: {response.text}")
        except Exception as e:
            print(f"Failed to register proxy {proxy_identity} with error: {e}")

    def report(self, message):
        if self.verbose:
            print(message)

    def submit_job_response(self, job_id, job_response):
        self.report(f"[PROXY] Submitting job response for job {job_id}")
        url = f"{self.proxy_host}{self.submit_job_proxy_endpoint.replace('*job_id', job_id)}"
        self.report(f"[PROXY] Submitting job response to {url}")
        headers = {"Authorization": f"Bearer {self.api_key}"}

        # Prepare the result field to match the expected StructuredResult enum
        structured_result = {
            "Generic": job_response  # Assuming job_response is the value you want to send
        }

        # Prepare the JSON body to match the expected CompleteJobEndpointArgs struct
        json_body = {
            "job_id": job_id,
            "result": structured_result
        }

        response = requests.post(url, headers=headers, json=json_body)  # Synchronous request
        if response.status_code == 200:
            self.report(f"[PROXY] Successfully submitted job response for job {job_id}")
        else:
            self.report(f"[PROXY] Failed to submit job response for job {job_id}")
            self.report(response.text)  # Log the response text to see the error message

    async def process_job(self, job):
        self.report(f"[PROXY] Processing job {job.id}, {job.request}")
        handler = self.handlers.get(job.request['url'])
        if handler:
            try:
                self.report(f"[PROXY] Running handler for job {job.id} with details {job.request}")
                job_response = handler(job.request['body'])  # Ensure your handlers are async if necessary
            except Exception as e:
                job_response = DryJobError(500, f"Error running handler for job {job.id} with details {job.request}: {e}")
        else:
            self.report(f"[PROXY] No handler for job {job.id} with details {job.request}, skipping.")
            job_response = DryJobError(404, f"No handler found for job {job.id} with details {job.request}")
        if isinstance(job_response, DryJobError):
            job_response = job_response.to_json()
        self.submit_job_response(job.id, job_response)

    def process_jobs(self, jobs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            tasks = [self.process_job(job) for job in jobs]
            loop.run_until_complete(asyncio.gather(*tasks))
        except Exception as e:
            self.report(f"[PROXY] Error processing jobs: {e}")
        finally:
            loop.close()

    def proxy_run(self):
        self.report("Starting DryProxy, a lightweight proxy server facilitating DryMerge integrations...")
        while True:
            url = f"{self.proxy_host}{self.get_jobs_proxy_endpoint.replace('*proxy_identity', str(self.proxy_identity))}"
            headers = {"Authorization": f"Bearer {self.api_key}"}
            try:
                self.report(f"[PROXY] Polling for jobs at {url}")
                response = requests.get(url, headers=headers,
                                        stream=True)  # Set stream=True to keep the connection open and long=True to
                # indicate long polling to the server
                if response.status_code == 200:
                    jobs_data = response.json().get("jobs", [])
                    jobs = [DryJob(job['id'], job['work']['Computer']) for job in jobs_data]
                    self.process_jobs(jobs)
                else:
                    self.report(f"[PROXY] Job queue endpoint responded with error: {response.text}")
            except Exception as e:
                self.report(f"[PROXY] Error polling for jobs: {e}")

    def start(self, run_proxy=True):
        if run_proxy:
            self.register_proxy()
            proxy_thread = Thread(target=self.proxy_run)
            proxy_thread.start()
