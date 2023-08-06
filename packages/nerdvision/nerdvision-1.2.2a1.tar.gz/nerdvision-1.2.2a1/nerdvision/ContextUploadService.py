import hashlib
import logging
from concurrent.futures.thread import ThreadPoolExecutor

import requests

from nerdvision import settings
from nerdvision.Utils import Utils

our_logger = logging.getLogger("nerdvision")


class ContextUploadService(object):
    def __init__(self, client_config):
        self.client_config = client_config
        self.url = settings.get_context_url()
        self.error_url = settings.get_error_url()
        self.api_key = settings.get_setting("api_key")
        self.version = 2
        self.pool = ThreadPoolExecutor(max_workers=2)
        self.pending = {}

    def send_event(self, event_snapshot):
        try:
            our_logger.debug("Sending snapshot to %s", self.url)
            query = '?breakpoint_id=' + event_snapshot['breakpoint']['breakpoint_id']
            query += '&workspace_id=' + event_snapshot['breakpoint']['workspace_id']
            if 'log_msg' in event_snapshot and event_snapshot['log_msg'] is not None:
                query += '&log_msg=' + event_snapshot['log_msg']

            return self.send_context('eventsnapshot', event_snapshot, query)
        except Exception:
            our_logger.exception("Error while sending event snapshot %s", self.url)

    def send_context(self, ctx_type, data, query=''):
        url = self.url + ctx_type + query

        data['version'] = self.version
        data['id'] = self.generate_id()

        return self.submit_task(url, data)

    def decorate(self, data):
        data['attributes'] = {}

        decorators = dict(self.client_config.decorators)
        for key in decorators.keys():
            decorator = decorators.get(key)
            try:
                name, decorator_data = decorator(data)
                data['attributes'][name] = decorator_data
            except:
                our_logger.exception("Decorator %s %s errored; removing.", key, decorator)
                self.client_config.remove_decorator(key)
        return data

    def pool_task(self, url, data):
        our_logger.debug('Task running in pool: %s', url)
        if settings.is_context_debug_enabled():
            our_logger.debug(data)
        response = requests.post(url=url, auth=(self.client_config.session_id, self.api_key), json=data)
        our_logger.debug("Context response: %s, %s", response, response.json)
        response.close()

    def send_skipped(self, skipped):
        return self.send_context('skipped', skipped)

    def send_profile(self, profile):
        return self.send_context("profile", profile)

    def send_nv_error(self, nv_error):
        return self.submit_task(self.error_url, nv_error.as_dict())

    def flush(self):
        if len(self.pending) > 0:
            for key in dict(self.pending).keys():
                self.pending[key].result(10)

    def generate_id(self):
        return hashlib.md5((self.client_config.session_id + Utils.generate_uid()).encode('utf-8')).hexdigest()

    def submit_task(self, url, data):
        future = self.pool.submit(self.pool_task, url, self.decorate(data))
        self.pending[data['id']] = future

        # cannot use 'del' in lambda: https://stackoverflow.com/a/41953232/5151254
        def callback(arg):
            if data['id'] in self.pending:
                del self.pending[data['id']]

        future.add_done_callback(callback)
        return future
