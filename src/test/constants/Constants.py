class Constants:
    def __init__(self):
        print("constants loaded")

    def app_url(self):
        return "https://app.vwo.com"

    @staticmethod # These methods can be used without creating an object
    def app_dashboard_url():
        return "https://app.vwo.com/#/dashboard"

    # Generally avoid using static as it is having problem with parallelism - one source multiple usage