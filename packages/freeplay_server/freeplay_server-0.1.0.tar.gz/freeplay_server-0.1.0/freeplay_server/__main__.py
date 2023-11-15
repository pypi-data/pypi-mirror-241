from freeplay_server.app import create_app_from_env
from freeplay_server.app_environment import AppEnvironment

env = AppEnvironment.from_env()

if __name__ == '__main__':
    create_app_from_env(env).run(debug=env.use_flask_debug_mode, host="0.0.0.0", port=env.port)
