public class LogLevels {

    public static String message(String logLine) {
        int colonIndex = logLine.indexOf(": ");
        if (colonIndex != -1) {
            return logLine.substring(colonIndex + 2).trim();
        }
        return logLine.trim();
    }

    public static String logLevel(String logLine) {
        int start = logLine.indexOf('[');
        int end = logLine.indexOf(']');
        if (start != -1 && end != -1 && end > start) {
            return logLine.substring(start + 1, end).toLowerCase();
        }
        return "";
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
