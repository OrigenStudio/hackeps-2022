import os
import argparse
import random
import json
import sys


def safe_open(_path, mode='w'):
    os.makedirs(os.path.dirname(_path), exist_ok=True)
    return open(_path, mode)


def init(args):
    challenge = args.challenge
    challenge_generator_fn = challenge_1 if challenge == 1 else challenge_2 if challenge == 2 else challenge_3
    for file_index in range(args.num_jsons):
        path = './assets/jsons/challenge_'+str(challenge)+'/generated_'+str(file_index + 1) + '.json'
        with safe_open(path) as fjson:
            json.dump(challenge_generator_fn(file_index), fjson)


def challenge_1(unused_file_index):
    num_orders = random.randint(5, 20)
    num_machines = random.randint(3, 10)

    machine_ids = []
    for machine_id in range(num_machines):
        machine_ids.append('mach::0'+str(machine_id))
    
    orders_list = []
    for order_id in range(num_orders):
        num_tasks = random.randint(1, 5)
        tasks = []
        for _ in range(num_tasks):
            tasks.append({
                "machine": random.choice(machine_ids),
                "duration": random.randint(1, 8)
            })
        orders_list.append(
            {
                "name": "order_" + str(order_id).rjust(4, '0'),
                "tasks": tasks
            }, )

    machines_list = [{"id": machine_id} for machine_id in machine_ids]
    return {"orders": orders_list, "machines": machines_list}


# { Machine id:  (task assignation probability, multiple) }
machines = {
    "printer_fdm": (10, False),
    "printer_mjf": (30, True),
    "hand_polish": (5, False),
    "tumble_polish": (15, True),
    "dyer": (25, True),
    "painter": (15, False),
}
# Min, max values for each random variable (it will be both inclusive [min, max])
NUM_ORDERS_BOUNDARIES = (200, 400)
NUM_TASKS_PER_ORDER_BOUNDARIES = (1, 4)
NUM_ITEMS_PER_TASK_BOUNDARIES = (1, 3)
ITEM_FREQUENCY = (5, 2, 3)


def get_boundaries(boundary: tuple[int, int],
                   inclusive=True) -> tuple[int, int]:
    return (boundary[0], boundary[1] if inclusive else boundary[1] - 1)


def get_random_choice_by_frequency(random_list_or_boundary,
                                   frequency_list,
                                   boundary=False):

    ## Inputs data: result list, acumulated frequency list (matches in lenght), and total Frequency
    results_list = [*range(*random_list_or_boundary)
                    ] if boundary else random_list_or_boundary
    acumulated_f = [
        sum(frequency_list[:y]) for y in range(1,
                                               len(frequency_list) + 1)
    ]
    Frequency = sum(frequency_list)

    ## Generate a random within Frequency range
    generated_choice = random.randint(1, Frequency)
    ## Get the index of the nearest ceiled integer in the frequency list
    index, _ = min(
        enumerate(acumulated_f),
        key=lambda freq: sys.maxsize
        if freq[1] < generated_choice else freq[1] - generated_choice)

    ## Return the result that matches that index
    return results_list[index]


def challenge_2(unused_file_index):
    machines_config_path = './assets/jsons/challenge_2/machines_config.json'
    machines_config = []
    with safe_open(machines_config_path, 'r') as machines_config_file:
        machines_config = json.load(machines_config_file)
    num_orders = random.randint(*get_boundaries(NUM_ORDERS_BOUNDARIES))

    orders = []
    for order_id in range(num_orders):
        num_tasks = random.randint(
            *get_boundaries(NUM_TASKS_PER_ORDER_BOUNDARIES))

        num_items = get_random_choice_by_frequency(
            [*get_boundaries(NUM_TASKS_PER_ORDER_BOUNDARIES)],
            ITEM_FREQUENCY,
            boundary=True)

        tasks = []
        used_machines_ids = []
        for task_id in range(num_tasks):
            available_machines = [
                (machine_config['id'], machines[machine_config['id']][0])
                for machine_config in filter(
                    lambda machine_config: num_items >= machine_config[
                        'max_items'] and machine_config['id'] not in
                    used_machines_ids, machines_config)
            ]
            if len(available_machines) <= 0: continue

            machine = get_random_choice_by_frequency(
                *map(list, zip(*available_machines)))
            used_machines_ids.append(machine)
            tasks.append({"task_number": task_id, "machine": machine})

        orders.append({
            "id": 'client::' + str(order_id).rjust(4, '0'),
            "quantity": num_items,
            "tasks": tasks
        })

    return {"orders": orders, "machines": machines_config}


def challenge_3(file_index):
    outputs_path = './assets/outputs/challenge_1'

    def csplit(l):
        return l[1:-1].split(',')

    machines_list = []

    lines = []
    output_path = 'output_'+str(file_index + 1)+'.txt'
    with open(os.path.join(outputs_path, output_path)) as f:
        lines = f.read().split('\n')

    for line_number, line in enumerate(lines):
        if not line.startswith('Machine'): continue
        mach_name = line.split('"')[1]
        machine_tasks = []
        next_line = line_number + 1

        while next_line + 1 < len(lines) and lines[next_line].startswith('\t'):
            task_str = lines[next_line].strip()
            split_by_dot = task_str.split('.')
            order, task_number = [
                res.strip() for res in csplit(split_by_dot[0])
            ]
            start, end = csplit(split_by_dot[-1])
            next_line += 1
            machine_tasks.append({
                "order": order,
                "task_number": task_number,
                "start_at": start,
                "end_at": end
            })
        machines_list.append({"id": mach_name, "tasks": machine_tasks})

    return machines_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-C',
        '--challenge',
        type=int,
        help='Number of challenge to generate JSONs',
        required=True,
        choices=[x + 1 for x in range(3)],
    )

    parser.add_argument(
        '-N',
        '--num-jsons',
        type=int,
        help='Number of files to generate',
        required=True,
    )
    args = parser.parse_args()
    init(args)