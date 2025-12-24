{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1214e2fa-af65-43fa-9caa-b3b369ee9c58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter student name:  Mehul J Chaudhary\n",
      "Enter marks (0-100):  85\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "📊 RESULT FOR MEHUL J CHAUDHARY:\n",
      "Marks: 85/100\n",
      "Grade: B\n",
      "Message: Very Good! Keep it up!\n"
     ]
    }
   ],
   "source": [
    "def calculate_grade(marks):\n",
    "    if marks >= 90:\n",
    "        return \"A\", \"Excellent work! Outstanding performance!\"\n",
    "    elif marks >= 80:\n",
    "        return \"B\", \"Very Good! Keep it up!\"\n",
    "    elif marks >= 70:\n",
    "        return \"C\", \"Good effort. Keep practicing!\"\n",
    "    elif marks >= 60:\n",
    "        return \"D\", \"You passed, but there is room for improvement.\"\n",
    "    else:\n",
    "        return \"F\", \"Don't give up. Learn from mistakes and try again!\"\n",
    "\n",
    "\n",
    "name = input(\"Enter student name: \").strip().upper()\n",
    "\n",
    "while True:\n",
    "    try:\n",
    "        marks = int(input(\"Enter marks (0-100): \"))\n",
    "        if 0 <= marks <= 100:\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid marks. Please enter marks between 0 and 100.\")\n",
    "    except ValueError:\n",
    "        print(\"Invalid input. Please enter numeric marks only.\")\n",
    "\n",
    "\n",
    "grade, message = calculate_grade(marks)\n",
    "\n",
    "print(\"\\n📊 RESULT FOR {}:\".format(name))\n",
    "print(f\"Marks: {marks}/100\")\n",
    "print(f\"Grade: {grade}\")\n",
    "print(f\"Message: {message}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1514df19-ce42-4d13-b909-250ffbc5d107",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "churn_env",
   "language": "python",
   "name": "churn_env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
