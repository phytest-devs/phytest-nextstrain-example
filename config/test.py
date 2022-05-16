from phytest import Alignment, Sequence, Tree

def test_alignment_size(alignment: Alignment):
    """
    By testing the size of our alignment we can 
    ensure that our pipeline won't run if there are 
    accidental sequence additions or deletions.
    """
    alignment.assert_length(34)
    alignment.assert_width(10769)

def test_sequence_no_gaps(sequence: Sequence):
    """
    We know that our sequences shouldn't have any
    gaps so we enforce this constrain to ensure the 
    quality of our alignment.
    """
    sequence.assert_count_gaps(0)

def test_tree_is_SG_monophyletic(tree: Tree):
    """
    We expect that all the samples from Singapore will 
    form a monophyletic clade in the tree.
    """
    singapore_tips = [tip for tip in tree.get_terminals() if 'SG_' in tip.name]
    tree.assert_is_monophyletic(singapore_tips)