use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let normalize = |s: &str| {
        let mut chars: Vec<char> = s.to_lowercase().chars().collect();
        chars.sort_unstable();
        chars
    };

    let word_norm = normalize(word);
    let word_lower = word.to_lowercase();

    possible_anagrams
        .iter()
        .filter(|&&candidate| {
            let candidate_lower = candidate.to_lowercase();
            let candidate_norm = normalize(candidate);
            candidate_lower != word_lower && candidate_norm == word_norm
        })
        .copied()
        .collect()
}
