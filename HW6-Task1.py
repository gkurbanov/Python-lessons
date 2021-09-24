import time


class TrafficLight:
    color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        x = 0
        for i in TrafficLight.color:
            print(f'Переключение светофора на {TrafficLight.color[x]}')
            if x == 0:
                time.sleep(7)
            elif x == 1:
                time.sleep(2)
            else:
                time.sleep(15)
            x += 1


trafficLight = TrafficLight()
trafficLight.running()
