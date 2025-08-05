import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.TextStyle;
import java.util.Locale;

class AppointmentScheduler {
    DateTimeFormatter parser = DateTimeFormatter.ofPattern("M/dd/yyyy HH:mm:ss");

    public LocalDateTime schedule(String appointmentDateDescription) {
        return LocalDateTime.parse(appointmentDateDescription, parser);
    }

    public boolean hasPassed(LocalDateTime appointmentDate) {
        return appointmentDate.isBefore(LocalDateTime.now()) ? true : false;
    }

    public boolean isAfternoonAppointment(LocalDateTime appointmentDate) {
        return appointmentDate.getHour() >= 12 && appointmentDate.getHour() < 18 ? true : false;
    }

    public String getDescription(LocalDateTime appointmentDate) {
        int minutes = appointmentDate.getMinute();
        int hour = appointmentDate.getHour();
        int day = appointmentDate.getDayOfMonth();
        int year = appointmentDate.getYear();
        String minutesString = minutes < 10 ? "0" + minutes : String.valueOf(minutes);
        String hourString = hour > 12 ? String.valueOf(hour - 12) : String.valueOf(hour);
        String dayOfWeekString = appointmentDate.getDayOfWeek().getDisplayName(TextStyle.FULL, Locale.US);
        String timeOfDay = hour < 12 ? "AM" : "PM";
        String monthString = appointmentDate.getMonth().getDisplayName(TextStyle.FULL, Locale.US);

        return "You have an appointment on " + dayOfWeekString + ", " + monthString + " " + day + ", " + year + ", at "
                + hourString + ":" + minutesString + " " + timeOfDay + ".";
    }

    public LocalDate getAnniversaryDate() {
        return LocalDate.of(LocalDate.now().getYear(), 9, 15);
    }
}
