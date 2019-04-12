# Making functions to mess with a dictionary of names to ages


class FamilyAgeUtils:

    def sort_by_age(group):    # sorts given dictionary by value
        sorted_group = sorted(group.items(), key=lambda kv: kv[1])
        return sorted_group

    def total_age(group):   # gives total value of given dictionary
        total = 0
        for age in group.values():
            total += age
        return total

    def average_age(group):     # gives the average value of given dictionary
        tot_age = 0
        group_total = 0
        for age in group.values():
            tot_age = tot_age + age
            group_total = group_total + 1
        return round(tot_age / group_total)

    def closest_age(group, input_age):      # finds the person with the closest age in given dictionary to given input
        age_list = sorted(group.values())
        nearest_age = age_list[0]
        answer_list = []
        for age in age_list:
            if age == input_age:
                nearest_age = age
                break
            if age == nearest_age:
                continue
            if abs(age - input_age) == abs(nearest_age - input_age):
                break
            if abs(age - input_age) < abs(nearest_age - input_age):
                nearest_age = age
                continue
        for name in group.keys():
            if group[name] == nearest_age:
                answer_list.append(name)
                continue
        return answer_list

    def total_age_div_by_2(group, add_even):   # gives total value of Odd or Even in given Dictionary
        total = 0
        if add_even:
            for age in group.values():
                if age % 2 == 0:
                    total += age
                else:
                    continue
        else:
            for age in group.values():
                if age % 2 == 1:
                    total += age
                else:
                    continue
        return total
