from datetime import datetime
class date_modify :
    def enforce_iso8601(self,iso_datetime):
        """
        Checks, validates, and returns the ISO 8601 formatted datetime string, 
        ensuring the date part is not less than the current date.

        Args:
            iso_datetime: The ISO 8601 formatted datetime string to validate (without trailing 'Z').

        Returns:
            The validated ISO 8601 formatted datetime string.

        Raises:
            ValueError: If the input format is invalid.
        """
        if iso_datetime == "":
            return ""
        try:
          # Try parsing as ISO 8601 format
          parsed_datetime = datetime.strptime(iso_datetime, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            try:
                # Try parsing as time format (e.g., "09:15:00")
                parsed_time = datetime.strptime(iso_datetime, "%H:%M:%S")
                # Get current date
                current_date = datetime.now().strftime("%Y-%m-%d")
                # Combine current date with parsed time
                return f"{current_date}T{iso_datetime}"
            except ValueError:
                raise ValueError("Invalid ISO 8601 format. Please provide a valid datetime string (YYYY-MM-DDTHH:MM:SS) or time string (HH:MM:SS).")

        current_date = datetime.now().strftime("%Y-%m-%d")  # Extract current date only
        parsed_date = parsed_datetime.date()
        if parsed_date < datetime.fromisoformat(current_date).date():
            # Replace date part with current date while keeping time
          return f"{current_date}T{parsed_datetime.strftime('%H:%M:%S')}"
        else:
          return iso_datetime