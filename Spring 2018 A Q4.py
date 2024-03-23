from threading import Thread, Lock
import os


def process_file(filename, lock, car_data):
    with open(filename, 'r') as file:
        for line in file:
            with lock:
                license_num, status = line.strip().split(',')
                if license_num not in car_data:
                    car_data[license_num] = 0

                else:
                    car_data[license_num] += 2


def create_files():
    # Data for each file
    data = [
        '12345678,0\n87654321,0\n',
        '12345678,0\n87654321,0\n',
        '12345678,1\n87654321,0\n',
        '87654321,0\n',
        '87654321,1\n',
        '123,0\n456,0\n',
        '123,0\n456,0\n',
        '123,1\n456,0\n',
        '456,0\n',
        '456,1\n'
    ]

    # Create cam_1.dat to cam_5.dat with data
    for (index, file_data) in enumerate(data):
        filename = f'cam_{index + 1}.dat'
        with open(filename, 'w') as f:
            f.write(file_data)


def main():
    car_data = {}
    lock = Lock()
    create_files()
    threads = [Thread(target=process_file, args=(f'cam_{i}.dat', lock, car_data))
               for i in range(1, 11)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    output = "costs.txt"
    with open(output, 'x') as file:
        for license_num, cost in car_data.items():
            file.write(f'{license_num} {cost}\n')


if __name__ == "__main__":
    main()
