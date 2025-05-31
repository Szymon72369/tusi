## 1. 📌 Project Overview

TUSI Web Page

The "TUSI Web Page" is a web application with a simple content management system (CMS) based on the Django admin panel. The **moderator** role has limited permissions to minimize the risk of accidentally deleting or damaging website content. Moderators can manage the majority of the website's content and choose the layout and color scheme of sections using predefined templates. **Only administrator accounts have access to system settings.**

------------------------------------------------

## 2. ⚙️ Tech Stack & Dependencies

* **Backend:** Python 3.13.1 + Django 5.2.1
* **Frontend:** HTML + Vanilla CSS + JavaScript
* **Database:** SQLite 3
* **Requirements:**

```
asgiref==3.8.1  
Django==5.2.1  
django-ckeditor==6.7.2  
django-filebrowser==4.0.3  
django-grappelli==3.0.10  
django-js-asset==3.1.2  
pillow==11.2.1  
six==1.17.0  
sqlparse==0.5.3  
tzdata==2025.2  
whitenoise==6.9.0  
```

---

## 3. 🧑‍💻 Setup Instructions

**Local environment:**

* Requirements: Python, pip, virtualenv

**Step-by-step:**

```bash
git clone tusi
py -m venv .venv
source .venv/Scripts/activate
cd tusi-web
pip install -r requirements.txt
py manage.py runserver
```

---

## 4. 🔐 Users and Roles

### **Administrator:**

* Full access

### **Moderator:**

A. Can view all sections **except** user and permission management
B. Can modify content in all available sections
C. Can add and delete entries in:

* Offer subpages
* Subpage content
* News
* Gallery
* About Us
* Offers
  D. Can change section **theme and color** via post list view in admin

---

## 5. 🧩 Features

### **CMS through Django Admin Panel**

**admin/**

* Admin path: `https://<domain>/admin/`

**home/**

* Landing page
* Editable entries via admin panel
* Automatically populated elements from subpages:

  * `gallery/`, `news/`, `about/`

**gallery/**

* CSS grid layout with image thumbnails and captions
* Clickable, zoomable images

**offer/**

* Editable entries via admin panel
* Automatically rendered sections for subpages using pattern: `../offer/slug/`
* Each generated section is a link to its corresponding subpage

---

## 6. 🧑‍⚖️ Content Management in CMS

### Editable fields and their purpose:

* **name:** internal label displayed in admin panel
* **title:** visible on the page as `<h2>`
* **text:** section content, rendered as `<p>`
* **button text / button link:** text shown on button and dropdown widget with auto-suggested internal links
* **file text / file:** link label and drag & drop file uploader
* **date:** optional date and time of the entry
* **style:** choose from several predefined section layouts
  ⚠️ Some layouts require an image – otherwise it won't appear on the page
* **color:** changes background color of the section
  ⚠️ Some themes also affect text and button color
* **order:** determines the display order both in admin and on the website

> ⚠️ **Warning:** Deleting an offer subpage (from `Offer_Subpages`) will delete **all related entries** in the subpage content section!
> Always be cautious when removing content in this app.
> **Deleting a category is irreversible.**

### CMS limitations:

* Each section supports **one image** and **one main heading** only

---

## 7. 🛠️ Maintenance

### Update project dependencies (via bash):

```bash
pip install -U -r requirements.txt
```

### Adding or removing offer subpages:

In the **"Offer Subpages"** section, add or remove an entry that includes:

* **name:** internal label in admin
* **title:** section header shown on the site
* **order:** display order (used for sorting in both the navigation dropdown and the admin panel)

> The system will **automatically generate** a slug based on the section name:
> `slug = section-name`
