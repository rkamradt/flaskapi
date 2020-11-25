import config


# Get the application instance
connex_app = config.connex_app
connex_app.add_api("swagger.yml")

if __name__ == "__main__":
    connex_app.run(debug=True)
