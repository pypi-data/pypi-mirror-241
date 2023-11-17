import click
import pathlib
from .pace import read_graph, read_solution

@click.command()
@click.option('--interleave', 'method', flag_value='interleave', help='Count crossings checking pairs of edges one by one.')
@click.option('--stacklike', 'method', flag_value='stacklike', help='Count crossings using a stack-like method, similar to counting crossings in book drawings.')
@click.option('--segtree', 'method', flag_value='segtree', default=True, help='Count crossings using a segment tree. [default]')
@click.option('-c', '--only-crossings', is_flag=True, default=False, help='Print only the found number of crossings.')
@click.argument('graph', type=click.Path(exists=True, path_type=pathlib.Path))
@click.argument('solution', type=click.Path(exists=True, path_type=pathlib.Path))
def verify(method, only_crossings, graph, solution):
    '''Print the amount of crossings the given solution has.'''
    solution = read_solution(solution)
    graph = read_graph(graph, solution)

    if method == "interleave":
        crossings = graph.countcrossings_trivial()
    elif method == "stacklike":
        crossings = graph.countcrossings_stacklike()
    else:
        crossings = graph.countcrossings_segtree()

    if only_crossings:
        print(crossings)
    else:
        print(f"Using {solution} as ordering of the vertices we found {crossings} crossings using the {method} method.")