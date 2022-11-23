# Origen studio challenges

Hello to our challenges! They are focused on "constraint programming" topic, and we seek to optimize the execution of certain tasks.

We structurize out challenge in three parts, each one can be done individually and independently from the others.

For this, we provide a template `main_pub.py` which we will execute, and a `generators.py` which creates even more inputs if you need them.

You can review the statements for each challenge at the botton of this README, as well as in the Hub Game.

## Requirements / Suggestions

Requirements:

- Nothing is stricly required. We provide a `python` files to execute, but if you have a better option, language, library... feel completly free to use!

Suggestions (not required):

- python3.9
- [Google OR tools](https://developers.google.com/optimization/scheduling/job_shop) library: C++, Python, C#, Java
- Based on [Google OR tools - Job Shop Problem](https://developers.google.com/optimization/scheduling/job_shop)
- Usage of virtual environments! `requirements.txt`,

## Virtual Environment

Our templates do not have any external dependencies.
For your custom libraries (or OR Tools library), you can access the virtual environment via

> $ source ./env/bin/activate

The virtual environment was installed using

> python3 venv env

## main_pub.py template

This template allows you to implement all the 3 challenges. To execute them, you specify the challenge number and the input file (JSON).

We will import execute the `main_pub.init` module, so follow its signature. You can modify the template according to your needs. If any important changes, please notify us (in a README).

Proposed usage:

> $ python3 main_pub.py [-h] -C {1,2,3} --input INPUT

```
optional arguments:
  -h, --help            show this help message and exit
  -C {1,2,3}, --challenge {1,2,3}
                        Number of challenge
  --input INPUT         Input file name path
```

## generators.py template

We provide you with one JSON per challenge. If you need more, you may use this tool to batch-create them (or by hand).

You may modify as much as you wish this file, adjusting the output directory, the boundaries, the names, etc, but we will avaluate using generated JSONs from this `generators.py`, with the procided configuration.

Usage:

> $ python3 generators.py [-h] -C {1,2,3} -N NUM_JSONS

```
optional arguments:
  -h, --help            show this help message and exit
  -C {1,2,3}, --challenge {1,2,3}
                        Number of challenge to generate JSONs
  -N NUM_JSONS, --num-jsons NUM_JSONS
                        Number of files to generate
```

### # Challenge 1

This challenge is an introduction to the goal. Although it is not required to perform the next challenges, it gives a certain amount of points and can be used as a warm-up.

### # Challenge 2

Can be done without the challenge 1, and it has additional constraints which can be found in the statement.

It is neither required to use the language nor the OR Tools we mentioned above. If you have a better idea, show off! It may give you extra points.

Also, if the optimal solution is way more complex to get than any solution, and you prove it, it would be even better!

Remember, we are giving you tips, but you are the professionals here! The more unique and valid steps you perform the higher score you would get.

### # Challenge 2 - Generator Notes

You can modify the generator file to adapt for your (testing) needs.

We will use the provided machine configuration file, at `line:50-57` // `line:96`, with the provided boundaries at `line:59-62`.

The generated JSON would be always random, with 200-400 orders, which they will have between 1-4 tasks.
Each task will have 1-3 items, with their frequency:
50% chance to get 1 item, 20% chance to get 2, and 30% for 3.

### # Challenge 3

All the data is optimized now, but it is still difficult to read.

This challenge aims to the create a visual interactive scheduler for the users to read all the data.

As previous ones, this challenge can be done individually, from the provided JSON.

The cooler and more unique features it has, the higher score it would be graded.

### # Challenge 3 - Generator Notes

The provided JSON is based on a simulated challenge 1 solution printed.
The generator tries to parse that soluction from a `.txt` file into the JSON, in the `/assets/outputs/challenge_1/` directory.
If you want different JSON inputs, you should create a similar txt format as the provided one, following this name format:

> output\_{index}.txt

Index is a positive integer, starting from 1.

When specifying the number of files to create, it should be equal or less than the output txt files.

_This generator is "hard-coded" for testing purposes. With the provided JSON it should be enough to perform the challenge_

_Reminder: if you manage to link the output of your challenge 2 with the input of challenge 3, that gives extra points_

## Final note

Remember this is a Hackathon!

We are here to have fun, thus we provide tips to follow, but the more creative and unique is your approach, as long it is well argumented, the better!

You may use any language or tool you feel comfortable.

# Appendix _Challenge Statements_

<h3>Challenge 1</h3>
<p><br></p>
<p>Based on &ldquo;The Job Shop Problem&rdquo; from Google OR-Tools. The problem is a constraint programming (CP) type which seeks for a time optimization of executing the jobs into different machines with given constraints: no overlapping, maximum one job per machine at the same time.</p>
<p><a href="https://developers.google.com/optimization/scheduling/job_shop">https://developers.google.com/optimization/scheduling/job_shop</a>&nbsp;</p>
<p><br></p>
<p>Manager X starts a new week in his work place at a manufacturing station. He received the orders to organize into the different machines for the following days. Besides, a moment ago he chit-chatted with his boss at the elevator. She mentioned they are planning to giveaway an organized trip for the most well-performing employees, thus X is thinking of optimizing the time of the orders.</p>
<p>An order has a set of tasks to execute, at least one task is present. The tasks within an order are dependent: task 2 cannot be executed until task 1 is completed; and each task has its own execution time for a specific machine.</p>
<p>These tasks require the usage of the machines available in the facility and, obviously, two different tasks assigned to the same machine cannot overlap in time.</p>
<p>For this, X wants a scheduling optimizer to split all the tasks from all the orders into the different machines and create a timetable for their execution. The received orders and their requirements and needs, as well as the available machines in the facility are grouped by him into the JSON file. Time units are in &ldquo;hours&rdquo;.</p>
<p>A list of the requirements and constraints is provided below:</p>
<ul>
    <li>
        <p>Read and process the JSON data.</p>
    </li>
    <li>
        <p>Provide the best solution: total number of hours.</p>
    </li>
    <li>
        <p>The tasks within an order must be executed in order; though it is not required instantly. Another task from another order may get in between. Every order has at least one task.</p>
    </li>
    <li>
        <p>Once a task starts its execution, it cannot be stopped until finished.</p>
    </li>
    <li>
        <p>The machines work at full capacity 24/7, without any time on starting and finishing the task on them.</p>
    </li>
    <li>
        <p>Each machine is specialized in only one task type, it cannot perform other tasks.</p>
    </li>
    <li>
        <p>There can only be one task at most being executed on a single machine.</p>
    </li>
</ul>
<br>
<br>
<h3>Challenge 2</h3>
<p><br></p>
<p>This problem follows the main idea of challenge 1, but in a more complex way. Challenge 2 can be done without necessarily doing challenge 1. Neither the results nor the inputs are the same, but you may code some utils which can be recycled for both challenges.</p>
<p><br></p>
<p>The boss was amazed by the optimization performed by X. She offered him an opportunity to implement a similar algorithm to a different department. In this scenario, the orders have a number of items to be created, which causes the machine execution time to be variable. Even though the machines can operate 24h a day, they need to be loaded during working hours, thus the start time of the machine must be within this range.</p>
<p>Workers&rsquo; shifts are from 9am to 5pm during weekdays (from Monday to Friday).</p>
<p>Additionally, as the machines are more complex, they require a fixed amount of time to prepare its execution and to clean it afterwards, which has to be done by the employees (during work hours).</p>
<p>The machines can operate grouping items from different orders, as long as the next task of that order uses the same machine, reducing the loading and unloading cost time.&nbsp;</p>
<p>The number of items that each machine can handle at the same time will be specified in their configuration file.&nbsp;</p>
<p>Important! Grouping items of different tasks is allowed, but the items of the same task must be done all at once. Order1 has 10 items, order2 has 5: possible executions are 15 at the same time, 10 and then 5 items, or first 5 and then 10, as long as the machine can handle a minimum of 15 items. It is not possible, for example, the execution of 7 items, and then 8.</p>
<p>The department requires an optimal (not necessarily the best) result in total hours and in days, always&nbsp;rounded up or ceil&nbsp;to the nearest unit&nbsp;(e.g. 5.3 days will be 6 days, 0.7 execution hours will be 1 hour, 3 days are 3 days). This result must include the machine idle hours.</p>
<p>The starting point is Monday at 9am.</p>
<p><br></p>
<p><br></p>
<p>A given example, the order for &ldquo;client01&rdquo; has the task &ldquo;Paint&rdquo; which needs to paint 34 items, and the execution time of the painting machine would be 0.5 hours per item, in total 17 hours. The machine needs 1 hour of preparation, and 2 of cleaning. Also, at this moment there is another order which its next task to execute is &ldquo;Paint&rdquo; 5 items with the same execution time per item.</p>
<p>Thus, the worker groups both tasks in the machine, a total of 39 items (19.5h execution time). He loads it at 9am for 1h, and the &ldquo;Paint&rdquo; starts executing at 10am, for 19:30h. It finishes at 5:30am the next day, but there are no workers until 9am, so at this time the worker unloads it until 11am.</p>
<p>The best result would be 26 total hours, 2 days.<br>Another feasible and valid result, as a sequential execution, would give 32 hours, 2 days.</p>
<p>The shorter the result, the better qualified, as long as the software execution time is short as well. The goal is to seek the best possible result calculated in a short period of time.</p>
<p><br></p>
<p>X accepts the offer and receives its first group of commands to optimize, along with all the machine data in a&nbsp;(different from challenge 1)&nbsp;JSON format.</p>
<p><br></p>
<ul>
    <li>
        <p>Provide&nbsp;ANY&nbsp;solution, rounded up in hours and the same solution in days.</p>
    </li>
    <li>
        <p>Machines work at full capacity 24/7. However they only can be started or ended between 9am-5pm during weekdays.</p>
    </li>
    <li>
        <p>Time execution is variable, depending on the items loaded from the tasks.</p>
    </li>
    <li>
        <p>The tasks within an order must be executed in order; though it is not required instantly. Another task from another order may get in between. Every order has at least one task.</p>
    </li>
    <li>
        <p>The items from different orders with the same task can be grouped together.</p>
    </li>
    <li>
        <p>Each machine is specialized in only one task type, it cannot perform other tasks.</p>
    </li>
    <li>
        <p>Machines&rsquo; &ldquo;execution_time&rdquo; is a variable formula. The provided characters are:</p>
        <ul>
            <li>
                <p>Positive numbers (either whole numbers e.g. 3 or one decimal numbers e.g. 5.1)</p>
            </li>
            <li>
                <p>Operations: *, +, -</p>
            </li>
            <li>
                <p>Items variable: x</p>
            </li>
            <li>
                <p>White spaces (can be ignored)</p>
            </li>
        </ul>
    </li>
</ul>
<p><br></p>
<p>The following aspects will be taken into consideration when qualifying:</p>
<ul>
    <li>
        <p>If it is the best solution. Discussion whether it is worth it to search for the best result, or is it too time consuming</p>
    </li>
    <li>
        <p>Implementation of custom algorithms, and usage of valid heuristics</p>
    </li>
    <li>
        <p>Gathered statistics related to the execution</p>
    </li>
</ul>
<br>
<br>
<h3>Challenge 3</h3>
<p><br></p>
<p>Employee Y arrives and reads her assigned tasks given from her manager X (from challenge 1). But she cannot interpret them and asks for a visualization tool of the timetable.</p>
<p>She would like an easy and pleasant usage, and with the ability to filter by the present data. For example: filter by machines, by quantity of items inside an order, task durations, tasks with due date for the next X hours/days&hellip;&nbsp;</p>
<p>We will assess the following content. Though it is not required, the more features the better qualification.</p>
<ul>
    <li>
        <p>Fancy design</p>
    </li>
    <li>
        <p>User eXperience and (low) amount of friction needed</p>
    </li>
    <li>
        <p>Original filter ideas and designs</p>
    </li>
    <li>
        <p>Whether interaction with the schedule view</p>
    </li>
    <li>
        <p>EXTRA POINTS: Implement a custom timetable using&nbsp;your&nbsp;results from challenge 2</p>
    </li>
</ul>
<p><br></p>
<p><br></p>
<p>A JSON file will be provided, which is a simulated output from challenge 1. The JSON is a list of machines, and their tasks to execute in order. Each task has a [start, end) interval (start included in task, end excluded).</p>
<ul>
    <li>
        <p>Assume machines can work at 24/7 capacity</p>
    </li>
    <li>
        <p>There is no loading / unloading time cost, to simplify the problem.</p>
    </li>
</ul>
