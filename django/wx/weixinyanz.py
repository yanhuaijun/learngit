import werobot

robot = werobot.WeRoBot(token='yhjtest')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8082

robot.run()
