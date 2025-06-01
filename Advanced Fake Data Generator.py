import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from faker import Faker
import csv
import openpyxl
import pyperclip
import random
from functools import partial

"""
This project for educational purpose, QA testing and so on 
made by Aaed Hany FarajAllah
Github : 3aed

"""

COUNTRY_CODES = {
    "Afghanistan": "+93",
    "Albania": "+355",
    "Algeria": "+213",
    "Andorra": "+376",
    "Angola": "+244",
    "Argentina": "+54",
    "Armenia": "+374",
    "Australia": "+61",
    "Austria": "+43",
    "Azerbaijan": "+994",
    "Bahrain": "+973",
    "Bangladesh": "+880",
    "Belarus": "+375",
    "Belgium": "+32",
    "Brazil": "+55",
    "Bulgaria": "+359",
    "Canada": "+1",
    "China": "+86",
    "Colombia": "+57",
    "Croatia": "+385",
    "Cyprus": "+357",
    "Czech Republic": "+420",
    "Denmark": "+45",
    "Egypt": "+20",
    "Estonia": "+372",
    "Finland": "+358",
    "France": "+33",
    "Germany": "+49",
    "Greece": "+30",
    "Hungary": "+36",
    "India": "+91",
    "Indonesia": "+62",
    "Iran": "+98",
    "Iraq": "+964",
    "Ireland": "+353",
    "Israel": "+972",
    "Italy": "+39",
    "Japan": "+81",
    "Jordan": "+962",
    "Kazakhstan": "+7",
    "Kuwait": "+965",
    "Lebanon": "+961",
    "Libya": "+218",
    "Malaysia": "+60",
    "Mexico": "+52",
    "Morocco": "+212",
    "Netherlands": "+31",
    "New Zealand": "+64",
    "Nigeria": "+234",
    "Norway": "+47",
    "Oman": "+968",
    "Pakistan": "+92",
    "Palestine": "+970",
    "Philippines": "+63",
    "Poland": "+48",
    "Portugal": "+351",
    "Qatar": "+974",
    "Romania": "+40",
    "Russia": "+7",
    "Saudi Arabia": "+966",
    "Singapore": "+65",
    "South Africa": "+27",
    "South Korea": "+82",
    "Spain": "+34",
    "Sweden": "+46",
    "Switzerland": "+41",
    "Syria": "+963",
    "Thailand": "+66",
    "Tunisia": "+216",
    "Turkey": "+90",
    "Ukraine": "+380",
    "United Arab Emirates": "+971",
    "United Kingdom": "+44",
    "United States": "+1",
    "Yemen": "+967"
}


COUNTRY_LOCALES = {
    "Afghanistan": "fa_AF",
    "Albania": "sq_AL",
    "Algeria": "ar_DZ",
    "Andorra": "ca_AD",
    "Angola": "pt_AO",
    "Argentina": "es_AR",
    "Armenia": "hy_AM",
    "Australia": "en_AU",
    "Austria": "de_AT",
    "Azerbaijan": "az_AZ",
    "Bahrain": "ar_BH",
    "Bangladesh": "bn_BD",
    "Belarus": "be_BY",
    "Belgium": "nl_BE",
    "Brazil": "pt_BR",
    "Bulgaria": "bg_BG",
    "Canada": "en_CA",
    "China": "zh_CN",
    "Colombia": "es_CO",
    "Croatia": "hr_HR",
    "Cyprus": "el_CY",
    "Czech Republic": "cs_CZ",
    "Denmark": "da_DK",
    "Egypt": "ar_EG",
    "Estonia": "et_EE",
    "Finland": "fi_FI",
    "France": "fr_FR",
    "Germany": "de_DE",
    "Greece": "el_GR",
    "Hungary": "hu_HU",
    "India": "hi_IN",
    "Indonesia": "id_ID",
    "Iran": "fa_IR",
    "Iraq": "ar_IQ",
    "Ireland": "en_IE",
    "Israel": "he_IL",
    "Italy": "it_IT",
    "Japan": "ja_JP",
    "Jordan": "ar_JO",
    "Kazakhstan": "kk_KZ",
    "Kuwait": "ar_KW",
    "Lebanon": "ar_LB",
    "Libya": "ar_LY",
    "Malaysia": "ms_MY",
    "Mexico": "es_MX",
    "Morocco": "ar_MA",
    "Netherlands": "nl_NL",
    "New Zealand": "en_NZ",
    "Nigeria": "en_NG",
    "Norway": "no_NO",
    "Oman": "ar_OM",
    "Pakistan": "ur_PK",
    "Palestine": "ar_PS",
    "Philippines": "fil_PH",
    "Poland": "pl_PL",
    "Portugal": "pt_PT",
    "Qatar": "ar_QA",
    "Romania": "ro_RO",
    "Russia": "ru_RU",
    "Saudi Arabia": "ar_SA",
    "Singapore": "en_SG",
    "South Africa": "en_ZA",
    "South Korea": "ko_KR",
    "Spain": "es_ES",
    "Sweden": "sv_SE",
    "Switzerland": "de_CH",
    "Syria": "ar_SY",
    "Thailand": "th_TH",
    "Tunisia": "ar_TN",
    "Turkey": "tr_TR",
    "Ukraine": "uk_UA",
    "United Arab Emirates": "ar_AE",
    "United Kingdom": "en_GB",
    "United States": "en_US",
    "Yemen": "ar_YE"
}


ID_FORMATS = {
    "United States": {"name": "SSN", "method": "ssn"},
    "Saudi Arabia": {"name": "IQAMA", "method": "iqama"},
    "Brazil": {"name": "CPF", "method": "cpf"},
    "India": {"name": "Aadhaar", "method": "aadhaar"},
}

SUPPORTED_LOCALES = Faker().locales


def generate_fake_data(locale, data_type, count=1, country_code=None):
    """Generates structured fake data based on locale and data type."""
    # Country based on key
    country = None
    if country_code == "Random":
        country = random.choice(list(COUNTRY_CODES.keys()))
        country_code = COUNTRY_CODES[country]
    elif country_code in COUNTRY_CODES.values():
        country = [k for k, v in COUNTRY_CODES.items() if v == country_code][0]
    else:
        country = "Saudi Arabia"
        country_code = COUNTRY_CODES[country]

    if locale == "ar_SA":
        selected_locale = "ar_SA"
    else:
        selected_locale = COUNTRY_LOCALES.get(country, "en_US")

    # check
    if selected_locale not in SUPPORTED_LOCALES:
        selected_locale = "ar_SA" if locale == "ar_SA" else "en_US"

    try:
        fake = Faker(selected_locale)
    except ValueError:
        fake = Faker("ar_SA" if locale == "ar_SA" else "en_US")

    # jops in AR
    arabic_jobs = [
        "مهندس", "طبيب", "معلم", "محاسب", "مبرمج", "مدير مشروع", "محامي", "طيار ", "مدير اعمال", "مقاول", "سباك", "", "مستشار قانوني"
    ]

    result = []

    for _ in range(count):
        data = {}

        if data_type == "Personal Info":
            phone_number = f"{country_code} {fake.msisdn()[3:]}"
            data = {
                "Name": fake.name(),
                "Address": fake.address().replace("\n", ", "),
                "Email": fake.email(),
                "Phone": phone_number,
                "Country": country,
                "Job": random.choice(arabic_jobs) if locale == "ar_SA" else fake.job(),
                "Company": fake.company(),
                "Random ID": random.randint(100000, 999999)
            }
        elif data_type == "Credit Card":
            data = {
                "Cardholder Name": fake.name(),
                "Card Provider": fake.credit_card_provider(),
                "Card Number": fake.credit_card_number(),
                "Card Security Code": fake.credit_card_security_code(),
                "Card Expiry Date": fake.credit_card_expire()
            }
        elif data_type == "Phone Number":
            phone_number = f"{country_code} {fake.msisdn()[3:]}"
            data = {
                "Country": country,
                "Phone Number": phone_number
            }
        elif data_type == "ID (Example)":
            id_format = ID_FORMATS.get(
                country, {"name": "Generic ID", "method": None})
            try:
                if id_format["method"] and hasattr(fake, id_format["method"]):
                    data = {id_format["name"]: getattr(
                        fake, id_format["method"])()}
                else:
                    data = {
                        "Generic ID": f"{random.randint(100000000, 999999999)}"}
            except AttributeError:
                data = {
                    "Generic ID": f"{random.randint(100000000, 999999999)}"}
        else:
            data = {"Error": "Invalid data type selected"}

        result.append(data)

    return result if count > 1 else result[0]


def format_data_for_display(data_list):
    """Formats the structured data dictionary for display in the text area."""
    formatted_string = ""
    for i, data in enumerate(data_list, 1):
        if len(data_list) > 1:
            formatted_string += f"=== Record #{i} ===\n"
        for key, value in data.items():
            formatted_string += f"{key}: {value}\n"
        formatted_string += "\n"
    return formatted_string.strip()


class FakeDataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Fake Data Generator")
        self.root.geometry("700x650")

        # --- Language Selection ---
        lang_frame = ttk.Frame(root)
        lang_frame.pack(pady=5)
        ttk.Label(lang_frame, text="Select Language:").pack(
            side=tk.LEFT, padx=5)
        self.language_var = tk.StringVar()
        self.language_combobox = ttk.Combobox(
            lang_frame,
            textvariable=self.language_var,
            values=["English", "Arabic"],
            state="readonly",
            width=10
        )
        self.language_combobox.pack(side=tk.LEFT, padx=5)
        self.language_var.set("English")
        self.language_combobox.bind(
            "<<ComboboxSelected>>", self.update_ui_for_language)

        # --- Country Selection (always visible) ---
        self.country_frame = ttk.Frame(root)
        self.country_frame.pack(pady=5)
        self.country_label = ttk.Label(
            self.country_frame, text="Select Country:")
        self.country_label.pack(side=tk.LEFT, padx=5)
        self.country_var = tk.StringVar()
        self.country_combobox = ttk.Combobox(
            self.country_frame,
            textvariable=self.country_var,
            values=["Random"] + sorted(COUNTRY_CODES.keys()),
            state="readonly",
            width=20
        )
        self.country_combobox.pack(side=tk.LEFT, padx=5)
        self.country_var.set("Random")

        # -3-A-E-D- Data Type Selection -3-A-E-D-
        dtype_frame = ttk.Frame(root)
        dtype_frame.pack(pady=5)
        ttk.Label(dtype_frame, text="Select Data Type:").pack(
            side=tk.LEFT, padx=5)
        self.data_type_var = tk.StringVar()
        self.data_type_combobox = ttk.Combobox(
            dtype_frame,
            textvariable=self.data_type_var,
            values=["Personal Info", "Credit Card",
                    "Phone Number", "ID (Example)"],
            state="readonly",
            width=15
        )
        self.data_type_combobox.pack(side=tk.LEFT, padx=5)
        self.data_type_var.set("Personal Info")

        # -3-A-E-D- Data Count Selection -3-A-E-D-
        count_frame = ttk.Frame(root)
        count_frame.pack(pady=5)
        ttk.Label(count_frame, text="Number of Records:").pack(
            side=tk.LEFT, padx=5)

        self.count_var = tk.StringVar()
        self.count_var.set("1")

        ttk.Radiobutton(
            count_frame,
            text="1",
            variable=self.count_var,
            value="1"
        ).pack(side=tk.LEFT, padx=2)

        ttk.Radiobutton(
            count_frame,
            text="Random (10-15)",
            variable=self.count_var,
            value="random"
        ).pack(side=tk.LEFT, padx=2)

        self.custom_count_entry = ttk.Entry(count_frame, width=5)
        self.custom_count_entry.pack(side=tk.LEFT, padx=2)

        ttk.Radiobutton(
            count_frame,
            text="Custom:",
            variable=self.count_var,
            value="custom"
        ).pack(side=tk.LEFT, padx=2)

        # Generate button
        self.generate_button = ttk.Button(
            root, text="Generate Data", command=self.display_fake_data)
        self.generate_button.pack(pady=10)

        # Output area with Scrollbar
        self.output_text = scrolledtext.ScrolledText(
            root, height=20, width=80, wrap=tk.WORD)
        self.output_text.pack(pady=10, padx=10)
        self.generated_data = []  # Store generated data

        # Action Buttons Frame
        action_frame = ttk.Frame(root)
        action_frame.pack(pady=10)
        ttk.Button(action_frame, text="Copy", command=self.copy_data_to_clipboard).pack(
            side=tk.LEFT, padx=10)
        ttk.Button(action_frame, text="Save As...",
                   command=self.save_data_to_file).pack(side=tk.LEFT, padx=10)

    def update_ui_for_language(self, event=None):
        """Updates UI based on language selection."""
        selected_language = self.language_var.get()
        if selected_language == "Arabic":
            arabic_countries = [
                k for k, v in COUNTRY_LOCALES.items() if v.startswith("ar_")
            ]
            self.country_combobox["values"] = [
                "Random"] + sorted(arabic_countries)
            self.country_var.set("Saudi Arabia")
        else:
            self.country_combobox["values"] = [
                "Random"] + sorted(COUNTRY_CODES.keys())
            self.country_var.set("Random")

    def display_fake_data(self):
        """Generates and displays fake data based on selections."""
        selected_language = self.language_var.get()
        selected_data_type = self.data_type_var.get()

        # Determine count
        if self.count_var.get() == "1":
            count = 1
        elif self.count_var.get() == "random":
            count = random.randint(10, 15)
        elif self.count_var.get() == "custom":
            try:
                count = int(self.custom_count_entry.get())
                if count < 1:
                    raise ValueError
            except ValueError:
                messagebox.showerror(
                    "Error", "Please enter a valid number (1 or more)")
                return
        else:
            count = 1

        locale = "en_US" if selected_language == "English" else "ar_SA"

        # Get country code
        selected_country = self.country_var.get()
        if selected_country == "Random":
            country_code = "Random"
        else:
            country_code = COUNTRY_CODES.get(selected_country, None)

        try:
            self.generated_data = generate_fake_data(
                locale,
                selected_data_type,
                count,
                country_code
            )

            # Convert single record to list for consistent processing
            data_list = [
                self.generated_data] if count == 1 else self.generated_data

            display_text = format_data_for_display(data_list)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, display_text)
        except Exception as e:
            self.output_text.delete(1.0, tk.END)
            messagebox.showerror("Error", f"Error generating data:\n{e}")
            self.generated_data = []

    def copy_data_to_clipboard(self):
        """Copies the content of the output text area to the clipboard."""
        data_to_copy = self.output_text.get(1.0, tk.END).strip()
        if data_to_copy:
            try:
                pyperclip.copy(data_to_copy)
                messagebox.showinfo("Copied", "Data copied to clipboard!")
            except Exception as e:
                messagebox.showerror(
                    "Clipboard Error", f"Could not copy to clipboard:\n{e}")
        else:
            messagebox.showwarning("No Data", "Nothing to copy.")

    def save_data_to_file(self):
        """Saves the generated data to file."""
        if not self.generated_data:
            messagebox.showwarning("No Data", "Generate data before saving.")
            return

        file_path = filedialog.asksaveasfilename(
            title="Save Data As",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("CSV files", "*.csv"),
                ("Excel files", "*.xlsx"),
                ("All files", "*.*")
            ]
        )

        if not file_path:
            return

        try:
            file_ext = file_path.split('.')[-1].lower()
            data_list = self.generated_data if isinstance(
                self.generated_data, list) else [self.generated_data]

            if file_ext == "txt":
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(format_data_for_display(data_list))
            elif file_ext == "csv":
                with open(file_path, "w", newline='', encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(data_list[0].keys())
                    for data in data_list:
                        writer.writerow(data.values())
            elif file_ext == "xlsx":
                wb = openpyxl.Workbook()
                ws = wb.active
                ws.append(list(data_list[0].keys()))
                for data in data_list:
                    ws.append(list(data.values()))
                for col in ws.columns:
                    max_length = 0
                    column = col[0].column_letter
                    for cell in col:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = (max_length + 2)
                    ws.column_dimensions[column].width = adjusted_width
                wb.save(file_path)
            else:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(format_data_for_display(data_list))

            messagebox.showinfo("Success", f"Data saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")


if __name__ == "__main__":
    try:
        import pyperclip
    except ImportError:
        print("Pyperclip not found. Clipboard functionality will be disabled.")

    root = tk.Tk()
    app = FakeDataApp(root)
    root.mainloop()
