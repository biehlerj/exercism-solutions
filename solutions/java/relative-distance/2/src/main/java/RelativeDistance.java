import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

class RelativeDistance {
    private final Map<String, Set<String>> familyTreeMap;

    RelativeDistance(Map<String, List<String>> familyTree) {
        this.familyTreeMap = new HashMap<>();

        for (Map.Entry<String, List<String>> familyTreeEntry : familyTree.entrySet()) {
            String parent = familyTreeEntry.getKey();
            List<String> children = familyTreeEntry.getValue();

            for (String child : children) {
                familyTreeMap.computeIfAbsent(parent, k -> new HashSet<>()).add(child);
                familyTreeMap.computeIfAbsent(child, k -> new HashSet<>()).add(parent);

                for (String sibling : children) {
                    if (!sibling.equals(child)) {
                        familyTreeMap.get(child).add(sibling);
                    }
                }
            }
        }
    }

    int degreeOfSeparation(String personA, String personB) {
        Queue<String> familyQueue = new ArrayDeque<>();
        Map<String, Integer> degreesOfSeparationMap = new HashMap<>();
        familyQueue.add(personA);
        degreesOfSeparationMap.put(personA, 0);

        while (!familyQueue.isEmpty()) {
            String currentFamilyMember = familyQueue.poll();
            int currentDegreesOfSeparation = degreesOfSeparationMap.get(currentFamilyMember);

            for (String relative : familyTreeMap.getOrDefault(currentFamilyMember, Set.of())) {
                if (!degreesOfSeparationMap.containsKey(relative)) {
                    degreesOfSeparationMap.put(relative, currentDegreesOfSeparation + 1);
                    familyQueue.add(relative);
                }
            }
        }

        return degreesOfSeparationMap.getOrDefault(personB, -1);
    }
}