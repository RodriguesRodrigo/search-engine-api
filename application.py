from application import create_app

app = create_app("default")

if __name__ == "__main__":
    ip = "0.0.0.0"
    port = app.config.get("APP_PORT", 5000)
    debug = app.config.get("DEBUG", False)

    app.run(
        host=ip,
        debug=debug,
        port=port,
        use_reloader=debug
    )
