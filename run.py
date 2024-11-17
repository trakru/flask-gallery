from app import create_app
from pyngrok import ngrok
import atexit

app = create_app()

if __name__ == '__main__':
    port = 8672

    # Open a ngrok tunnel
    public_url = ngrok.connect(port).public_url
    print(f" * ngrok tunnel available at {public_url}")

    # Set the public URL
    app.config['PUBLIC_URL'] = public_url

    # ngrok exit with app
    def shutdown_ngrok():
        ngrok.kill()

    atexit.register(shutdown_ngrok)

    # Run app
    app.run(port=port)
