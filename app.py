# Main entry point of the MVC application

from controllers.home_controller import HomeController

if __name__ == '__main__':
    app = HomeController()
    app.run()