from pathlib import Path

# TODO: This is getting huge, maybe separate it into multiple config files using YAML or TOML

project_root: Path = Path(__file__).parent / ".."
datasets_root: Path = project_root / "datasets"

# Place to store models downloaded from Hugging Face Hub
models_root: Path = project_root / "models"
codet5_small = models_root / "codet5-small"
codet5_base = models_root / "codet5-base"

cache_dir: Path = project_root / ".cache"

coconut_data_dir: Path = datasets_root / "CoCoNuT"
coconut_java2006: Path = coconut_data_dir / "java/2006"
coconut_python2010: Path = coconut_data_dir / "python/2010"
coconut_javascript2010: Path = coconut_data_dir / "javascript/2010"
coconut_c2005: Path = coconut_data_dir / "c/2005"

coconut_preprocessed_data_dir: Path = datasets_root / "CoCoNuT_Preprocessed"

quixbugs_dir: Path = datasets_root / "QuixBugs"
quixbugs_python_buggy_dir: Path = quixbugs_dir / "python_programs"
quixbugs_python_correct_dir: Path = quixbugs_dir / "correct_python_programs"
quixbugs_java_buggy_dir: Path = quixbugs_dir / "java_programs"
quixbugs_java_correct_dir: Path = quixbugs_dir / "correct_java_programs"
quixbugs_genpy_dir: Path = datasets_root / "GeneratedQuixBugs/python"
quixbugs_genjava_dir: Path = datasets_root / "GeneratedQuixBugs/java"
quixbugs_programs: list[str] = [
    "bitcount",
    "breadth_first_search",
    "bucketsort",
    "depth_first_search",
    "detect_cycle",
    "find_first_in_sorted",
    "find_in_sorted",
    "flatten",
    "gcd",
    "get_factors",
    "hanoi",
    "is_valid_parenthesization",
    "kheapsort",
    "knapsack",
    "kth",
    "lcs_length",
    "levenshtein",
    "lis",
    "longest_common_subsequence",
    "max_sublist_sum",
    "mergesort",
    "minimum_spanning_tree",
    "next_palindrome",
    "next_permutation",
    "pascal",
    "possible_change",
    "powerset",
    "quicksort",
    "reverse_linked_list",
    "rpn_eval",
    "shortest_path_length",
    "shortest_path_lengths",
    "shortest_paths",
    "shunting_yard",
    "sieve",
    "sqrt",
    "subsequences",
    "to_base",
    "topological_ordering",
    "wrap",
]

tree_sitter_lib: Path = project_root / "tools/tree-sitter-lib"
