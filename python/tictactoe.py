from random import randint, seed
from time import sleep

seed()
Color = str
Hex = str
reset = "\033[m"


def clamp(val: int, mn: int,
          mx: int) -> int: return mx if val > mx else mn if val < mn else val


def color(r: int, g: int, b: int) -> Color:
    r = clamp(r, 0, 255)
    g = clamp(g, 0, 255)
    b = clamp(b, 0, 255)

    return f"\033[38;2;{r};{g};{b}m"


def clr(color_: Hex) -> Color:
    return color(int(color_[1:3], 16), int(color_[3:5], 16), int(color_[5:7], 16))


c0 = clr("#00A500")  # -> "\033[38;2;0;165;0m
c1 = clr("#C20000")  # -> "\033[38;2;195;0;0m"
c2 = clr("#D930A2")
c3 = clr("#B6D6B6")  # -> "\033[38;2;150;150;150m"
c4 = clr("#FFA500")  # -> "\033[38;2;255;165;0m"
c5 = clr("#2F80A0")
c6 = clr("#C22055")


class Player:
    __mark: chr
    __color: Color
    __id: int | None

    def __init__(self, mark: chr, color: Color, id: int):
        self.__mark = mark
        self.__color = color
        self.__id = id

    def move(self) -> str:
        return self.__mark

    def smove(self) -> int:
        return self.__id

    def show_color(self):
        return self.__color


class Field:
    __field: [[Player]]
    __moves: int
    __lmove: int
    __taken: (int)

    def __init__(self):
        self.new()

    def show(self):
        print(c3)
        print("\t\t\t +----------+")
        print(f"\t\t\t |  MOVE {c1}{self.__moves}{c3}  |")
        print("\t\t\t +----------+")
        print(reset)

        print(f"\t\t\t{c3}+---+---+---+{reset}")
        for i in range(3):
            for j in range(3):
                print(f"\t\t\t{c3}|{reset}" * (j == 0) + " ", end="")
                print(self.__field[i][j].show_color()
                      if i * 3 + j != self.__lmove else c4,
                      self.__field[i][j].move(), sep="", end=reset)
                print(f" {c3}|{reset}", end="")

            print(f"\n\t\t\t{c3}+---+---+---+{reset}")

    def move(self, pos: [1, 2, 3, 4, 5, 6, 7, 8, 9], player: Player):
        self.__moves += 1
        pos -= 1
        self.__lmove = pos

        self.__taken.add(pos + 1)

        self.__field[pos // 3][pos % 3] = player
        self.show()

    def check_winner(self) -> [bool, [0, 1, 2, 3, 4, 5, 6, 7, 8]]:
        if self.__field[0][0].smove() is not None:
            if self.__field[0][0].smove() == self.__field[0][1].smove() == self.__field[0][2].smove():
                return [True, self.__field[0][0].smove()]
            if self.__field[0][0].smove() == self.__field[1][0].smove() == self.__field[2][0].smove():
                return [True, self.__field[0][0].smove()]

        if self.__field[1][1].smove() is not None:
            if self.__field[0][0].smove() == self.__field[1][1].smove() == self.__field[2][2].smove():
                return [True, self.__field[1][1].smove()]
            if self.__field[0][1].smove() == self.__field[1][1].smove() == self.__field[2][1].smove():
                return [True, self.__field[1][1].smove()]

            if self.__field[0][2].smove() == self.__field[1][1].smove() == self.__field[2][0].smove():
                return [True, self.__field[1][1].smove()]
            if self.__field[1][0].smove() == self.__field[1][1].smove() == self.__field[1][2].smove():
                return [True, self.__field[1][1].smove()]

        if self.__field[2][2].smove() is not None:
            if self.__field[0][2].smove() == self.__field[1][2].smove() == self.__field[2][2].smove():
                return [True, self.__field[2][2].smove()]
            if self.__field[2][0].smove() == self.__field[2][1].smove() == self.__field[2][2].smove():
                return [True, self.__field[2][2].smove()]

        return [False, -1]

    def new(self):
        self.__moves = 0
        self.__lmove = -1
        self.__field = [[Player(str(i * 3 + j + 1), c5, None)
                         for j in range(3)]for i in range(3)]
        self.__taken = set()

    def allowed_move(self, pos: int) -> bool:
        return pos not in self.__taken


def main():
    plrs = [Player('X', c1, 0), Player('O', c0, 1), Player('-', c4, 2)]
    fld = Field()

    i = 0
    fld.show()

    while not fld.check_winner()[0]:
        print(c3, "\t\t -> ", plrs[i % 2].show_color(), plrs[i %
              2].move(), c3, " to move.", sep="")
        print(c3, "\t\tPlease enter position where you")
        print("\t\t\twant to make move:")
        pos = input(f"\t\t\t{c2}[1; 9]{c3}: {c2}")
        print(reset, end="")
        if pos.isdigit() and 0 < int(pos) < 10 and fld.allowed_move(int(pos)):
            pos = int(pos)

            fld.move(pos, plrs[i % 2])

            if i == 8:
                break
            i += 1

    print(c3)
    sleep(0.1)
    print("""
             __    __ _
            / / /\\ \\ (_)_ __  _ __   ___ _ __
            \\ \\/  \\/ / | '_ \\| '_ \\ / _ \\ '__|
             \\  /\\  /| | | | | | | |  __/ |
              \\/  \\/ |_|_| |_|_| |_|\\___|_|
    """)
    sleep(0.25)
    print("""
                          _
                         (_)
                          _ ___
                         | / __|
                         | \\__ \\
                         |_|___/
     """, reset)

    sleep(0.65)
    print(c3, "\t\t\t  +---+", reset)
    print(c3, "\t\t\t  | ", plrs[fld.check_winner()[1]].show_color(),
          plrs[fld.check_winner()[1]].move(), c3, " |", reset, sep="")
    print(c3, "\t\t\t  +---+", reset)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(reset)
        print(c6, "\t\tSOMETHING WENT WRONG!", reset)
        print(reset, c3, "\t\t", err, reset)
    except KeyboardInterrupt as err:
        print(reset)
        print(c6, "\n\tBye-Bye, LOOSER!!!")
        print("\t QUITING THIS EASY GAME!!!")
        print("\t  HOW DARE YOU BE SO WEAK!!!", reset)
        print(reset, c3, "\t\t", err, reset)
    else:
        sleep(0.5)
        print(c3)
        if randint(0, 10) < 9:
            print("""
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠴⠒⠤⣄⡀⠀⠀⠀⠀⢠⣾⠉⠉⠉⠉⠑⠒⠦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠉⠲⡄⠀⢠⠏⡏⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢤⣤⣀⡀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⢸⠀⡇⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠈⠙⠢⣄⠀⠀⣿⠀⠀⠀⢰⣿⣷⣆⠀⠀⠀⠘⣾⠀⠇⠀⠀⠀⢾⣿⣿⣦⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⢀⣀⡤⣄⠀⠀⠀⣼⡇⠀⠀⠀⢀⣀⠀⠀⠀⠈⠳⣴⢿⡄⠀⠀⢸⡿⣿⢹⠀⠀⠀⠀⣿⠀⡆⠀⠀⠀⣼⠻⣇⣸⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⢀⡴⠚⠉⠀⠀⠈⠳⡄⠀⣿⡇⠀⠀⠀⣿⣿⡷⡄⠀⠀⠀⢹⣆⢧⠀⠀⠀⠙⠿⠋⠀⠀⠀⠀⣿⠀⡇⠀⠀⠀⠙⠛⠉⠁⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⢠⠟⠀⠀⠀⠀⢀⣤⣾⣷⣀⡇⢣⠀⠀⠀⢻⣟⣄⣷⠀⠀⠀⠈⣿⣾⣆⠀⠀⠀⠀⠀⠀⠀⠀⣸⢿⢰⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⣠⡏⠀⠀⠀⣼⡟⣿⣿⡿⠛⠉⢻⣞⣧⠀⠀⠀⠉⠛⠁⠀⠀⠀⠀⡿⣿⣿⣦⣀⠀⠀⠀⠀⣠⣾⡏⢸⣠⣧⣤⣄⣤⣤⣤⣤⣤⣴⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⣿⠀⠀⠀⢸⠋⣿⠛⠁⠀⠀⠀⠀⠻⣯⣷⣄⠀⠀⠀⠀⠀⠀⢀⣼⠁⠘⠿⣿⣿⣻⣿⣿⣿⣿⠏⠀⣾⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⡟⣇⠀⠀⠈⢿⣏⢧⣴⣶⡆⠀⠀⠀⢿⣿⣿⢳⢦⣤⣤⣤⣶⣿⠟⠀⠀⠀⠀⠉⠉⠛⠋⢩⡤⠖⠒⠛⠛⡿⢁⣾⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣷⠀⠀⠀⠀⢀⣤⠤⠤⣀⡀⠀
 ⣇⠘⣆⠀⠀⠀⠙⠻⠿⠛⠃⠀⠀⠀⣸⡙⠻⢿⣿⣿⣿⣿⠿⠋⠀⣀⡤⠤⠒⠚⠳⣄⢠⣿⠁⠀⠀⠀⢠⠇⡏⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⢀⡴⢫⡇⠀⠀⠀⠈⠙
 ⠘⣶⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⣀⣼⣿⠇⠀⠀⠀⣀⣀⣀⠀⢀⣼⣿⣦⡀⠀⠀⠀⠈⢻⡏⠀⠀⠀⠀⡞⠀⡇⢸⠀⠀⠀⠀⢰⣾⣶⣶⣶⣶⣶⡏⠀⠀⡼⠀⡞⠀⠀⠀⠀⠀⢸
 ⠀⠈⠻⣿⣿⣿⣶⢶⡶⡶⣶⣾⣿⡿⠋⣠⠴⠚⠉⠁⠀⠉⠙⠺⡿⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⣸⠃⢰⠀⢸⠀⠀⠀⠀⠘⠛⠛⠿⠿⢿⡏⠀⠀⢰⠃⢠⠇⠀⠀⠀⠀⠀⠌
 ⠀⠀⠀⠈⠙⠻⠿⠼⠽⠿⠿⠟⠋⢰⡟⠁⠀⠀⢀⣤⣄⡀⠀⠀⠹⡆⠙⢿⣿⣿⣦⡀⠀⠀⠀⠀⢰⡇⠀⢸⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡞⠀⡜⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⢳⡀⠀⠀⠈⢿⡿⠇⠀⠀⣼⠃⠀⠀⠙⢿⣿⣿⣷⠀⠀⠀⠈⡇⠀⢸⠀⡄⠀⠀⠀⠀⢰⣶⣤⣤⣤⣼⠃⠀⢰⠃⢰⠃⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⢣⠀⠀⠀⠀⠀⠀⠀⠈⠋⠉⠲⣄⠀⠀⠙⢿⠸⡄⠀⠀⠀⢳⠀⢸⠀⡇⠀⠀⠀⠀⠸⣿⣿⣿⣿⣃⠀⠀⣞⣠⣾⣤⣀⣀⠀⠀⡄⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠈⣇⠀⠀⠀⠀⣠⣤⣀⠀⠀⠀⠘⣆⠀⠀⠸⡄⢳⠀⠀⠀⠸⡆⢸⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⠻⢿⣿⣿⣿⣿⡿⠞⠁⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠘⡄⠀⠀⠀⢻⣿⣿⠆⠀⠀⠀⢸⠀⠀⠀⣇⠘⡆⠀⢀⣀⣧⢸⢀⣿⣶⣤⣤⣤⣀⣀⣀⠀⢀⡏⠀⢀⣴⠟⠁⠀⠀⠈⢳⡀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠹⡄⠀⠀⠈⠉⠁⠀⠀⠀⣠⡾⠀⠀⠀⢹⢀⣿⣿⣿⡿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⢰⣯⡏⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠹⡄⠀⠀⠀⢀⣠⣴⣾⣿⠃⠀⠀⠀⠘⠿⠟⠛⠛⠁⠀⠀⠀⠉⠉⠉⠛⠛⠛⠿⠟⠁⠀⠀⢾⣿⣷⣄⡀⠀⠀⢀⡼⠃⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⢳⣴⣶⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣦⣿⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⣀⠀⠀⠀⠀⠀⠀⠀

            """)
        else:
            print("""
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⢾⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠋⣀⣼⡏⣼⣏⣹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣶⣿⣿⣿⣡⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⢾⣿⣿⣿⣿⣟⠋⣉⣉⠙⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠁⣀⣴⣿⣿⣿⠿⢿⣿⠿⣿⣿⠟⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠔⠚⠛⣇⣀⣠⣴⣿⠿⠋⠹⣿⣤⣾⣿⡦⣽⠇⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⢀⣤⣶⣿⠋⠀⢸⣿⣿⣿⣾⡟⠋⠉⠁⠀⠀⠀⢹⣿⣿⠛⠛⠂⢀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⢀⣴⡟⢹⣿⠇⠀⣠⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣶⣿⣴⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⢠⣾⠋⠠⡿⠋⣠⣾⣿⣿⣿⣿⣡⣤⣤⣄⡤⣊⣭⣿⣿⣿⣮⣍⣿⡿⠛⠉⢀⣸⣧⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀
           ⢻⣷⡆⠀⠀⣈⠁⠀⠴⠿⠿⠿⠿⣿⢿⣿⣿⣿⡿⠛⠛⠛⢿⣿⣿⣷⠴⣾⣿⣿⣿⣷⣦⡄⠑⢤⡀⠀⠀⠀⠀
           ⠈⠻⣿⣿⣿⣿⣿⣗⣀⣠⣤⣤⡀⠀⢀⣿⣿⣯⣀⣠⡆⠀⠈⢿⠋⠀⠾⠿⠿⠿⣿⣿⣿⣿⣶⣾⡿⠳⡀⠀⠀
           ⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣶⣤⣼⠀⢰⠀⠀⠀⠉⢁⡀⠀⠘⣿⡿⣁⠴⢳⣄⠀
           ⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⡦⢬⡛⠻⠿⣿⣿⣿⡄⢾⣶⣶⣾⣯⣿⡆⠀⠀⡉⠁⠹⣷⣿⢿⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⡇⢸⣷⣄⣀⣠⣼⣿⠃⣰⣿⣿⣿⣿⣿⣷⡀⢠⣇⠀⢰⣿⣿⣌⡇
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣧⣾⣿⣿⣿⣿⣿⡿⡄⢻⣿⣿⣿⡉⢻⣿⣷⣸⣿⢠⡟⠀⠙⢿⡄
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⢀⣷⢸⣿⣿⣿⣷⣾⣿⣿⣿⣿⡿⠀⣤⠀⠘⡇
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠟⣠⣾⣇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣾⣿⠀⠀⣇
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣏⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡴⢀⣿
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠙⠒⠒⠛⠿⢿⣿⣿⣿⣿⣟⡛⠛⠿⠿⣿⣿⣿⣿⣿⡿⣡⣿⣿
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣶⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠟⢿⣿⣿⣿⠟⢻⣿
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣼⣿⣿⣿⠀⣋⣿

            """)
        print(reset)
