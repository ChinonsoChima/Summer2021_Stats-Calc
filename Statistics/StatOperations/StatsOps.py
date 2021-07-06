from Calculator.Operations.operations import Operations


class StatsOps:

    def __init__(self):
        pass

    @staticmethod
    def mean(data):
        if len(data) == 0:
            return "Error: empty data list"
        try:
            data_len = len(data)
            total = sum(data)
            return float(Operations.division(data_len, total))
        except ZeroDivisionError:
            return "Error: Can't Divide by zero"
        except TypeError:
            return "Error: Check your data values"
        except ValueError:
            return "Error: check data value"

    @staticmethod
    def median(data):
        if len(data) == 0:
            return "Error: empty data list"
        try:
            list_len = len(data)
            list_sort = sorted(data)
            index = (list_len - 1) // 2

            if list_len % 2 == 1:
                return float(list_sort[index])
            else:
                return float((list_sort[index] + list_sort[index + 1]) / 2)

        except ZeroDivisionError:
            return "Error: Can't Divide by zero"
        except TypeError:
            return "Error: Check your data values"
        except ValueError:
            return "Error: check data value"

    @staticmethod
    def mode(data):
        if len(data) == 0:
            return "Error: empty data list"
        try:
            counter = 0
            num = data[0]

            for i in data:
                curr_frequency = data.count(i)
                if curr_frequency > counter:
                    counter = curr_frequency
                    num = i

            return float(num)

        except ZeroDivisionError:
            return "Error: Can't Divide by zero"
        except TypeError:
            return "Error: Check your data values"
        except ValueError:
            return "Error: check data value"

    @staticmethod
    def variance(data):
        if len(data) == 0:
            return "Error: empty data list"
        try:
            data_mean = StatsOps.mean(data)
            x = 0

            for num in data:
                x = x + Operations.square(num - data_mean)

            return float(Operations.division(len(data), x))

        except ZeroDivisionError:
            return "Error: Can't Divide by zero"
        except TypeError:
            return "Error: Check your data values"
        except ValueError:
            return "Error: check data value"

    @staticmethod
    def std_deviation(data):
        if len(data) == 0:
            return "Error: empty data list"
        try:
            data_variance = StatsOps.variance(data)
            return float(Operations.square_root(data_variance))

        except ZeroDivisionError:
            return "Error: Can't Divide by zero"
        except TypeError:
            return "Error: Check your data values"
        except ValueError:
            return "Error: check data value"

    @staticmethod
    def z_score(data):
        if len(data) == 0:
            return "Error: empty data list"
        try:
            data_mean = StatsOps.mean(data)
            data_sd = StatsOps.std_deviation(data)
            z_score_list = []
            for num in data:
                z_score = (num - data_mean) / data_sd
                z_score_list.append(round(z_score, 4))
            return z_score_list

        except ZeroDivisionError:
            return "Error: Can't Divide by zero"
        except TypeError:
            return "Error: Check your data values"
        except ValueError:
            return "Error: check data value"