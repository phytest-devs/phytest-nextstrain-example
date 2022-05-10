from phytest import Alignment, Sequence, Tree


def test_alignment_size(alignment: Alignment):
    alignment.assert_length(34)
    alignment.assert_width(10769)

def test_no_gaps(sequence: Sequence):
    sequence.assert_count_gaps(0)

def test_sequences_only_contains_standard_characters(sequence: Sequence):
    sequence.assert_valid_alphabet('ACTGNKWY')

def test_tree_tips(tree: Tree):
    tree.assert_number_of_tips(34)

def test_tree_is_bifurcating(tree: Tree):
    tree.assert_is_bifurcating()