
class Register:

    @staticmethod
    def cash_register(cost, money_paid):
        if money_paid < cost:
            raise Exception('Insufficient funds')
        change = {}
        change_left = (money_paid * 100) - (cost * 100)
        while change_left != 0:
            while change_left >= 5000:
                if '£50' not in change:
                    change['£50'] = 1
                    change_left -= 5000
                else:
                    change['£50'] += 1
                    change_left -= 5000
            while change_left >= 2000:
                if '£20' not in change:
                    change['£20'] = 1
                    change_left -= 2000
                else:
                    change['£20'] += 1
                    change_left -= 2000
            while change_left >= 1000:
                if '£10' not in change:
                    change['£10'] = 1
                    change_left -= 1000
                else:
                    change['£10'] += 1
                    change_left -= 1000
            while change_left >= 500:
                if '£5' not in change:
                    change['£5'] = 1
                    change_left -= 500
                else:
                    change['£5'] += 1
                    change_left -= 500
            while change_left >= 100:
                if '£1' not in change:
                    change['£1'] = 1
                    change_left -= 100
                else:
                    change['£1'] += 1
                    change_left -= 100
            while change_left >= 50:
                if '50p' not in change:
                    change['50p'] = 1
                    change_left -= 50
                else:
                    change['50p'] += 1
                    change_left -= 50
            while change_left >= 20:
                if '20p' not in change:
                    change['20p'] = 1
                    change_left -= 20
                else:
                    change['20p'] += 1
                    change_left -= 20
            while change_left >= 10:
                if '10p' not in change:
                    change['10p'] = 1
                    change_left -= 10
                else:
                    change['10p'] += 1
                    change_left -= 10
            while change_left >= 5:
                if '5p' not in change:
                    change['5p'] = 1
                    change_left -= 5
                else:
                    change['5p'] += 1
                    change_left -= 5
            while change_left >= 1:
                if '1p' not in change:
                    change['1p'] = 1
                    change_left -= 1
                else:
                    change['1p'] += 1
                    change_left -= 1
        return change

    @staticmethod
    def cash_register2(cost, money_paid):
        if money_paid < cost:
            raise Exception('Insufficient funds')
        change = {}
        change_list = {
            '£50': 5000,
            '£20': 2000,
            '£10': 1000,
            '£5': 500,
            '£1': 100,
            '50p': 50,
            '20p': 20,
            '10p': 10,
            '5p': 5,
            '1p': 1
        }
        change_left = (money_paid * 100) - (cost * 100)
        for m in change_list.keys():
            while change_left >= change_list[m]:
                if m not in change:
                    change[m] = 1
                    change_left -= change_list[m]
                else:
                    change[m] += 1
                    change_left -= change_list[m]
        return change

