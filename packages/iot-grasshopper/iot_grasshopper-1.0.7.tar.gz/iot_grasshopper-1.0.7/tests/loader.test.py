from greengrass import automatic_loader
import time

if __name__ == '__main__':
    configurer = AutoConfigurer(5)
    time.sleep(30)
    configurer.close()
