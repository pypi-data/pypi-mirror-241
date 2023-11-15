from collections import namedtuple


class Profile:
    def __init__(self):
        self.v1_profile = 'v1/profile'
        self.v2_profile = 'v2/profile'

    def __del__(self):
        pass


class Node:
    def __init__(self):
        self.v1_node = 'v1/node'
        self.v2_node = 'v2/node'
        self.v1_node_id = 'v1/node/{nodeId}'
        self.v1_node_id_reboot = 'v1/node/{nodeId}/reboot'
        self.notifications = 'v2/notification/node/{nodeId}/event'
        self.stats = 'v1/report/node/{nodeId}/stats'
        self.stats_summary = 'v1/report/node/{nodeId}/stats'
        self.upgrade = 'v1/node/{nodeId}/upgrade'
        self.convert_to_cluster = 'v1/node/{nodeId}/convert-to-cluster'
        self.hw_monitoring = 'v1/node/{nodeId}/monitoring'
        self.trafficinsight = 'v1/node/{nodeId}/trafficinsight'
        self.v1_node_id_command = 'v1/node/{nodeId}/{Command}'
        self.v1_node_id_command_history_cli_id = 'v1/node/{nodeId}/{Command}/history/{cliId}'


class Cluster:
    def __init__(self):
        self.v1_cluster_id = 'v1/cluster/{clusterId}'
        self.v2_cluster = 'v2/cluster'
        self.v1_cluster = 'v1/cluster'
        self.v1_cluster_upgrade = 'v1/cluster/{clusterId}/upgrade'
        self.v1_cluster_trafficinsight = 'v1/cluster/{clusterId}/trafficinsight'


class Download:
    def __init__(self):
        self.v1_download_event = 'v1/download/event'
        self.v1_download_event_id = 'v1/download/event/{eventId}'
        self.v1_download_activity = 'v1/download/activity'
        self.v1_download_activity_id = 'v1/download/activity/{activityId}'
        self.v1_node_id_download = 'v1/node/{nodeId}/download'


class FirewallGroup:
    def __init__(self):
        self.v1_firewallgroup = 'v1/firewallgroup'
        self.v1_firewallgroup_id = 'v1/firewallgroup/{firewallgroupId}'
        self.v2_firewallgroup = 'v2/firewallgroup'


class Image:
    def __init__(self):
        self.v1_image_id = 'v1/node/{nodeId}/image/{imageId}'
        self.v2_image = 'v2/node/{nodeId}/image'


class Network:
    def __init__(self):
        self.v1_network = 'v1/network'
        self.v2_network = 'v2/network'
        self.v1_network_id = 'v1/network/{networkId}'
        self.v1_network_id_resetcounter = 'v1/network/{networkId}/resetcounter'


class Authenticate:
    def __init__(self):
        self.v1_authenticate = 'v1/authenticate'
        self.v1_logout = 'v1/logout'


class Org:
    def __init__(self):
        self.v1_org = 'v1/org'
        self.v1_user_current = 'v1/user/current'
        self.v2_org = 'v2/org'
        self.v1_org_id = 'v1/org/{orgId}'
        self.v1_org_id_policy = 'v1/org/{orgId}/policy'


class Pki:
    def __init__(self):
        self.v1_pki = 'v1/pki'
        self.v2_pki = 'v2/pki'


class Secret:
    def __init__(self):
        self.v1_secret = 'v1/secret'
        self.v1_secret_id = 'v1/secret/{secretId}'
        self.v2_secret = 'v2/secret'


class Service:
    def __init__(self):
        self.v1_service = 'v1/service'
        self.v1_service_id = 'v1/service/{serviceId}'
        self.v2_service = 'v2/service'
        self.v2_servicetemplate = 'v2/servicetemplate'
        self.v1_servicetemplate_id = 'v1/servicetemplate/{templateId}'
        self.v1_service_id_restart = 'v1/service/{serviceId}/restart'
        self.v1_listener_id = 'v1/listener/{listenerId}'
        self.v2_listener = 'v2/listener'
        self.v1_listener = 'v1/listener'
        self.v1_listener_id = 'v1/listener/{listenerId}'


class Sshkey:
    def __init__(self):
        self.v2_sshkey = 'v2/sshkey'
        self.v1_sshkey = 'v1/sshkey'
        self.v1_sshkey_id = 'v1/sshkey/{sshkeyId}'


class User:
    def __init__(self):
        self.v2_user = 'v2/user'
        self.v1_user = 'v1/user'
        self.v1_user_id = 'v1/user/{userId}'
        self.v2_notifications = 'v2/notification'
        self.v2_mysubscriptions = 'v2/mysubscriptions'
        self.v1_mysubscriptions = 'v1/mysubscriptions'
        self.v1_mysubscriptions_id = 'v1/mysubscriptions/{subId}'
        self.v1_webhook = 'v1/webhook'
        self.v2_webhook = 'v2/webhook'
        self.v1_webhook_id = 'v1/webhook/{webhookId}'
        self.v1_webhook_id_verify = 'v1/webhook/{webhookId}/verify'
        self.v1_webhook_id_test = 'v1/webhook/{webhookId}/test'
