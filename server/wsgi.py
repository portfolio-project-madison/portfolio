from server.app import create_app

app = create_app()

if __name__ == '__main__':
    import os 
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=True)