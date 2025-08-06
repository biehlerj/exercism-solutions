import java.util.HashSet;
import java.util.List;
import java.util.Set;

class GottaSnatchEmAll {

    static Set<String> newCollection(List<String> cards) {
        return new HashSet<>(cards);
    }

    static boolean addCard(String card, Set<String> collection) {
        return collection.add(card);
    }

    static boolean canTrade(Set<String> myCollection, Set<String> theirCollection) {
        Set<String> myUniqueCards = new HashSet<>(myCollection);
        Set<String> theirUniqueCards = new HashSet<>(theirCollection);
        myUniqueCards.removeAll(theirCollection);
        theirUniqueCards.removeAll(myCollection);

        return !myUniqueCards.isEmpty() && !theirUniqueCards.isEmpty();
    }

    static Set<String> commonCards(List<Set<String>> collections) {
        Set<String> commonCardSet = new HashSet<>();

        if (!collections.isEmpty()) {
            commonCardSet.addAll(collections.get(0));
            collections.forEach(commonCardSet::retainAll);
        }

        return commonCardSet;
    }

    static Set<String> allCards(List<Set<String>> collections) {
        Set<String> combinedCollection = new HashSet<>();

        for (Set<String> collection : collections) {
            for (String card : collection) {
                combinedCollection.add(card);
            }
        }

        return combinedCollection;
    }
}
