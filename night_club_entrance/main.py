import night_club_entrance.helper as helper


class Bouncer:
    def should_i_kick_him_out(self, age: int) -> bool:

        if age < 18:
            return True
        else:
            return False


if __name__ == '__main__':

    helper.print_nice_banner()

    bouncer = Bouncer()

    if bouncer.should_i_kick_him_out(age=17):
        print('why are u even trying to get in ??')
    else:
        print('let him in')
