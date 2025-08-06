public class LogLine {
    String logLine;

    public LogLine(String logLine) {
        this.logLine = logLine;
    }

    public LogLevel getLogLevel() {
        int start = logLine.indexOf('[') + 1;
        int end = logLine.indexOf(']');
        String levelName = logLine.substring(start, end);

        return LogLevel.fromLevel(levelName);
    }

    public String getOutputForShortLog() {
        LogLevel logLevel = getLogLevel();
        String logMessage = logLine.substring(logLine.indexOf(':') + 1);

        return logLevel.getLevelNumber() + ":" + logMessage.strip();
    }
}
