import java.util.List;
import java.util.Map;

class RelativeDistance {
    Map<String, List<String>> familyTree;

    RelativeDistance(Map<String, List<String>> familyTree) {
        this.familyTree = familyTree;
    }

    int degreeOfSeparation(String personA, String personB) {
        List<String> personAList = this.familyTree.get(personA);
        // List<String> personBList = this.familyTree.get(personB);
        int degreesOfSeparation = 0;

        for (String person : personAList) {
            if (person != null) {
                degreesOfSeparation++;
            }
        }

        return degreesOfSeparation;
    }
}
