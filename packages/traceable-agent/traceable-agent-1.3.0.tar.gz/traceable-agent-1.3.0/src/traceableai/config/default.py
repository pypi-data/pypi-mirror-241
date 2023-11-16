DEFAULT = {
    'opa': {
        'enabled': False,
        'endpoint': 'http://localhost:8181',
        'poll_period_seconds': 30,
    },
    'blocking_config': {
        'enabled': True,
        'debug_log': False,
        'evaluate_body': True,
        'modsecurity': {
            'enabled': True
        },
        'skip_internal_request': True,
        'regionBlocking': {
            'enabled': True
        },
        'max_recursion_depth': 20
    },
    'remote_config': {
        'enabled': True,
        'endpoint': 'localhost:5441',
        'poll_period_seconds': 30,
    }
}
