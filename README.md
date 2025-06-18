# 🔢 K-th Smallest Element: Insertion Sort vs Merge Sort

This project compares the performance of **Insertion Sort** and **Merge Sort** in finding the **k-th smallest element** of a randomly generated list. The goal is to evaluate how each sorting algorithm behaves as the list size increases, using repeated measurements for benchmarking.

---

## 📁 Project Structure

* `insertion.py` – Uses Insertion Sort to sort the list and find the k-th smallest element.
* `merge.py` – Uses Merge Sort to sort the list and retrieve the k-th smallest element.

---

## ⚙️ How It Works

Each script:

1. Generates random lists of different sizes.
2. Selects a random valid `k` for each list.
3. Sorts the list using the chosen algorithm.
4. Retrieves the `k-th` smallest element.
5. Measures and prints:

   * Average execution time
   * Maximum execution time
   * List size
   * Tested `k` values (for Merge Sort)

---

## 🧪 Example Output

```
List size: 5000
Average time: 0.4321 seconds
Max time: 0.4902 seconds
-----------------------------
```

---

## 💻 Requirements

* Python 3.x
* No external dependencies (uses only `random`, `time` and built-in functions)

---

## 👤 Author

Cláudio Alves Gonçalves de Oliveira
Email: [hi@claudioav.com](mailto:hi@claudioav.com)

---

## 📄 License

This project is licensed under the MIT License.
