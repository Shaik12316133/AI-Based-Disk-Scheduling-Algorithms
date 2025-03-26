# **Disk Scheduling Algorithms Simulator**  
**A Python GUI application to visualize and compare disk scheduling algorithms (FCFS, SSTF, SCAN, Q-Learning, Genetic Algorithm).**  

---

## **📌 Features**  
✔ **Multiple Algorithms**:  
   - **FCFS** (First-Come-First-Serve)  
   - **SSTF** (Shortest Seek Time First)  
   - **SCAN** (Elevator Algorithm)  
   - **Q-Learning** (AI-based optimization)  
   - **Genetic Algorithm** (Evolutionary optimization)  

✔ **Interactive GUI** with real-time visualization  
✔ **Performance Metrics**:  
   - Seek Time  
   - Response Time  
   - Throughput  
✔ **Workload Patterns**:  
   - Random  
   - Sequential  
   - Reverse  
   - Custom  
✔ **Save/Load Configurations**  

---

## **🚀 Installation**  
### **Prerequisites**  
- Python 3.8+  
- `tkinter` (usually included with Python)  
- `matplotlib`  

### **Setup**  
1. Clone the repository:  
   ```sh
   git clone https://github.com/yourusername/disk-scheduling-simulator.git
   cd disk-scheduling-simulator
   ```  
2. Install dependencies:  
   ```sh
   pip install matplotlib numpy
   ```  
3. Run the application:  
   ```sh
   python disk_scheduling_app.py
   ```  

---

## **🎮 Usage**  
1. **Select an algorithm** (FCFS, SSTF, SCAN, etc.)  
2. **Set initial head position** (e.g., `100`)  
3. **Enter requests** (comma-separated, e.g., `45, 80, 130, 170, 220`)  
4. **Click "Start"** to run the simulation  
5. **View results**:  
   - Seek sequence  
   - Seek time  
   - Response time  
   - Throughput  
6. **Visualize disk head movement** in the embedded graph  

### **Buttons**  
- **Start**: Run the simulation  
- **Route**: Show the seek path  
- **Return**: Reset head to initial position  
- **Reset**: Clear all inputs  
- **Save Config**: Save current settings  
- **Load Config**: Load saved settings  
- **Help**: Display usage instructions  

---

## **📊 Test Cases**  
| Test Case | Input (Requests, Head) | Algorithm | Expected Seek Time |
|-----------|------------------------|-----------|--------------------|
| Basic FCFS | `45, 80, 130, 170, 220`, `100` | FCFS | `230` |
| SSTF Optimization | `45, 80, 130, 170, 220`, `100` | SSTF | `230` |
| SCAN (Elevator) | `45, 80, 130, 170, 220`, `100` | SCAN | `295` |
| Empty Requests | `(none)`, `100` | FCFS | `0` |
| Single Request | `150`, `100` | SSTF | `50` |

---

## **🛠 Future Improvements**  
- [ ] Add **C-SCAN** and **LOOK** algorithms  
- [ ] Implement **automated testing** with `unittest`  
- [ ] Add **dark/light theme** toggle  
- [ ] Export results to **CSV/Excel**  
- [ ] Support **real-time disk simulation**  

---

## **📜 License**  
This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for details.  

---

## **📧 Contact**  
- **Author**: Shaik Baba Sameer  
- **Email**: babasameer32@gmail.com.com
  
---

### **🎉 Happy Scheduling!**  
Optimize disk I/O like a pro! 🚀  

---
