import json

import qiskit
from qiskit.compiler import assemble
from qiskit.providers import  BackendV1
from qiskit.providers.provider import ProviderV1
from qiskit.providers.job import JobV1 as Job
from qiskit.providers.models import BackendConfiguration
 
from qiskit_aer import AerSimulator
from qiskit.providers.options import Options

import os
import time 
import random
import string 
import warnings
import api

class QuantierJob(Job):
    def __init__(self, backend, circuit, **kwargs):
        self.job_backend = backend 
        self.job_json = self.assemble_and_prepare_job(circuit, **kwargs)
        self.job_id = self.generate_string()
        self._http_client = backend._http_client
        
        super().__init__(job_backend, job_id=self.job_id) # Use actual job_id as per your requirements
    
    def generate_string(self):
        backend_name = self.job_backend.name()  
        timestamp = int(time.time() * 1000) 
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Random string of length 8
        return f"jobId-{backend_name}-{timestamp}-{random_string}"
    
    def assemble_and_prepare_job(self, circuit, **kwargs):
        job = assemble(circuit).to_dict()
        job['header']['backend_name'] = self.job_backend.name()
        job['header']['backend_version'] = self.job_backend.configuration().backend_version
        job['config']['shots'] = kwargs.get('shots', 5)
        job['config']['memory'] = kwargs.get('memory', "True")
        job['config']['init_qubits'] = kwargs.get('init_qubits', "True")
        job['config']['parameter_binds'] = kwargs.get('parameter_binds', [])
        return json.dumps(job)

    # Following are the mandatory methods to be implemented for a Job.
    def result(self, timeout=10):
        
        post_obj = {
            'job_id': self.job_id
        }

        resp = self._http_client.post('/job/getresult', json=post_obj)
        self.result = resp.result
        
        if self.result is None:
            warnings.warn("Job excution not finished. Check the status and try again later")
        else:
            return self.result

    def cancel(self):
        pass  # implement your logic here

    def status(self):
        post_obj = {
            'job_id': self.job_id
        }
    
        resp = self._http_client.post('/job/getstatus', json=post_obj)
        self.status = resp.status
        
        return self.status

    def backend(self):
        return self._backend

    def job_id(self):
        return self.job_id  # implement your logic here

    def submit(self):
        pass  # implement your logic here

    def print(self):
        return self.job_json
     
    def job_dict(self):
        return self.job_dict

# Initiate a job
# Save the job to the backend server DB
# Queue the job
class QuantierBackend(BackendV1):
    def __init__(self, provider):
        configuration = BackendConfiguration(
            backend_name='QUANTierBackend',
            backend_version='1.1.0',
            n_qubits=32,
            basis_gates=['x', 'y', 'z', 'h', 'cx', 'id'],
            simulator=True,
            local=True,
            conditional=False,
            open_pulse=False,
            memory=True,
            max_shots=1024,
            max_experiments=1,
            gates=[],
            coupling_map=None
        )
        self._http_client = provider._http_client
        super().__init__(configuration=configuration)
    
    # Save your job to the QUANTier backend server
    def _save_job(self, job):

        post_obj = {  
          "job_id": job.job_id,
          "job_json": job.job_json
        }

        resp = self._http_client.post('/job/savejob', json=post_obj)
        resp.raise_for_status()

        json_resp = json.loads(resp.content.decode('utf-8'))
        
    
    def _queue_job(self, job):
        
        self._save_job(job)

        post_obj = {  
          "job_id": job.job_id,
          "job_json": job.job_json
        }

        resp = self._http_client.post('/job/queuejob', json=post_obj)
        resp.raise_for_status()

        json_resp = json.loads(resp.content.decode('utf-8'))        
          
    def run(self, circuit, **kwargs):        
        
        job = QuantierJob(self, circuit, **kwargs)
        
        self._queue_job(job)
    
        return job
   
    @classmethod
    def _default_options(cls):
        return Options()


# Authenticates users. 
# Show available backends (including the simulator).
# Connects to backend for authorization. 
class QuantierProvider(ProviderV1):

    DEFAULT_API_URL: Final = "20.205.139.227"
    BACKEND_LIST : Final = ['AerSimulator, QUANTierBackend'] 

    def __init__(self, access_token=None):
        super().__init__()

        API_base_url = os.environ.get("QUANTier_API_URL", QuantierProvider.DEFAULT_API_URL)
        self.api_url = f"{DEFAULT_API_URL}"
        self.access_token = access_token
        self.name = 'quantier_provider'

        if not self.access_token:
            warnings.warn(
                "No access token provided: access is restricted to the 'local simulators'."
            )
    
    @property
    def _http_client(self) -> httpx.Client:
        """HTTP client for communicating with the Quantier API."""
        return api.http_client(base_url=self.api_url, token=self.access_token)
    
    def backends(self, **kwargs):
        with self._http_client as client:
            resp = client.get('/backends')
            resp.raise_for_status()

        #To Do: Add /backends api. Return all accessible backends names for the user.    
        return self._backends = resp.backends

    def get_backend(self, name=None, **kwargs):
        if name.lower() == 'AerSimulator':
            return self._simulator
        elif name.lower() == 'QUANTierBackend':
            return QuantierBackend(self)
        else:
            raise qiskit.providers.exceptions.QiskitBackendNotFoundError('Backend not found')


        
        