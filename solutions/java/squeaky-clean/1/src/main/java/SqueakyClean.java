class SqueakyClean {
    static String clean(String identifier) {
        StringBuilder cleaned = new StringBuilder(identifier.length());

        for (int i = 0; i < identifier.length(); i++) {
            if (identifier.charAt(i) == ' ') {
                cleaned.append('_');
            } else if (identifier.charAt(i) == '-') {
                cleaned.append(Character.toUpperCase(identifier.charAt(i + 1)));
                i++;
            } else if (identifier.charAt(i) == '4') {
                cleaned.append('a');
            } else if (identifier.charAt(i) == '3') {
                cleaned.append('e');
            } else if (identifier.charAt(i) == '0') {
                cleaned.append('o');
            } else if (identifier.charAt(i) == '1') {
                cleaned.append('l');
            } else if (identifier.charAt(i) == '7') {
                cleaned.append('t');
            } else if (!Character.isLetter(identifier.charAt(i))) {
                continue;
            } else {
                cleaned.append(identifier.charAt(i));
            }
        }
        return cleaned.toString();
    }
}
