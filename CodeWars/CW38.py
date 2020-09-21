class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = [list(x) for x in queues]
        self.capacity = capacity
        pass

    def theLift(self):
        queues = self.queues
        cap = self.capacity
        floors = len(queues)
        order = [0]
        elevator = []
        wait = True

        while wait:
            wait = False
            for floor in range(floors):
                stop = False
                for person in elevator[:]:
                    if person == floor:
                        elevator.remove(person)
                        stop = True
                for person in queues[floor][:]:
                    if person > floor :
                        stop = True
                        if cap > len(elevator):
                            elevator.append(person)
                            queues[floor].remove(person)
                        else:
                            wait = True
                if stop and not order[-1] == floor:
                    order.append(floor)


            for floor in range(len(queues) -1, -1, -1):
                stop = False
                for person in elevator[:]:
                    if person == floor:
                        elevator.remove(person)
                        stop = True
                for person in queues[floor][:]:
                    if person < floor:
                        stop = True
                        if cap > len(elevator):
                            elevator.append(person)
                            queues[floor].remove(person)
                        else:
                            wait = True
                if stop and not order[-1] == floor:
                    order.append(floor)

        if order[-1] != 0:
            order.append(0)

        return order





if __name__ == '__main__':

    lift = Dinglemouse(((), (), (5, 5, 5), (), (), (), ()), 5)
    print(lift.theLift())