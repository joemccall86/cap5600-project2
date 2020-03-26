from town import Town


class Experiment:
    @staticmethod
    def run(towns):
        print('Running simulation with towns: ')
        for town in towns:
            print("Town " + town.name + " with population " + str(town.population))


if __name__ == '__main__':
    # Information on area towns from Wikipedia
    pensacola = Town('Pensacola', 52_713)
    navarre = Town('Navarre', 44_876)
    ferry_pass = Town('Ferry Pass', 28_921)
    pace = Town('Pace', 34_215)
    milton = Town('Milton', 10_269)

    Experiment().run([pensacola, navarre, ferry_pass, pace, milton])
