import java.util.regex.Matcher;
import java.util.regex.Pattern;

class SqueakyClean {
    static String clean(String identifier) {
        StringBuilder cleaned = new StringBuilder(identifier.length());
        String noSpaces = identifier.replaceAll("\\s", "_");
        Matcher unKebabed = Pattern.compile("-(\\w)").matcher(noSpaces);

        while (unKebabed.find()) {
            unKebabed.appendReplacement(cleaned, unKebabed.group(1).toUpperCase());
        }

        unKebabed.appendTail(cleaned);
        String compiledUnKebabed = cleaned.toString();
        String noLeet = compiledUnKebabed.replaceAll("4", "a")
                .replaceAll("3", "e")
                .replaceAll("0", "o")
                .replaceAll("1", "l")
                .replaceAll("7", "t");
        String noNonLetters = noLeet.replaceAll("[^a-zA-Z_]", "");

        return noNonLetters;
    }
}
