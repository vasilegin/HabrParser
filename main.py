import click
from parser.db.base import DB

from multiprocessing.dummy import Pool as ThreadPool
from datetime import datetime
from parser.parse import worker

@click.group()
def main():
    pass


@click.command()
@click.option('--min', default=0, help='Минимальный id статей')
@click.option('--max', default=1000000, help='Максимальный id статей')
@click.option('--threads', default=3, help='Количество потоков')
def start(min, max, threads):
    pool = ThreadPool(threads)
    start_time = datetime.now()
    results = pool.map(worker, range(min, max))
    pool.close()
    pool.join()
    print(datetime.now() - start_time)

if __name__ == '__main__':
    start()