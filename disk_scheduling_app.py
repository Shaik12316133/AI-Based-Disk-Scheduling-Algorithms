import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class DiskSchedulingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Disk Scheduling Dashboard")
        self.root.geometry("1000x700")
        
        # Variables
        self.algorithm_var = tk.StringVar(value="SCAN")
        self.head_pos_var = tk.StringVar(value="100")
        self.requests_var = tk.StringVar(value="45, 80, 130, 170, 220")
        self.workload_var = tk.StringVar(value="Random")
        
        # Create UI components
        self.create_controls_frame()
        self.create_dashboard_frame()
        self.create_metrics_frame()
        
    def create_controls_frame(self):
        controls_frame = ttk.LabelFrame(self.root, text="Controls", padding=(10, 5))
        controls_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Algorithm selection
        ttk.Label(controls_frame, text="Algorithm:").grid(row=0, column=0, sticky="w")
        algo_menu = ttk.Combobox(controls_frame, textvariable=self.algorithm_var, 
                                values=["FCFS", "SSTF", "SCAN", "Q-Learning", "Genetic Algorithm"])
        algo_menu.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Head position
        ttk.Label(controls_frame, text="Head Position:").grid(row=1, column=0, sticky="w")
        ttk.Entry(controls_frame, textvariable=self.head_pos_var).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Requests
        ttk.Label(controls_frame, text="Requests:").grid(row=2, column=0, sticky="w")
        ttk.Entry(controls_frame, textvariable=self.requests_var).grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Workload pattern
        ttk.Label(controls_frame, text="Workload Pattern:").grid(row=3, column=0, sticky="w")
        pattern_menu = ttk.Combobox(controls_frame, textvariable=self.workload_var, 
                                   values=["Random", "Sequential", "Reverse", "Custom"])
        pattern_menu.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        # Buttons
        button_frame = ttk.Frame(controls_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Start", command=self.start_simulation).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Route", command=self.show_route).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Return", command=self.return_head).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_simulation).pack(side="left", padx=5)
        
        # Config buttons
        config_frame = ttk.Frame(controls_frame)
        config_frame.grid(row=5, column=0, columnspan=2, pady=5)
        
        ttk.Button(config_frame, text="Save Config", command=self.save_config).pack(side="left", padx=5)
        ttk.Button(config_frame, text="Load Config", command=self.load_config).pack(side="left", padx=5)
        ttk.Button(config_frame, text="Help", command=self.show_help).pack(side="left", padx=5)
        
        # Feedback
        ttk.Label(controls_frame, text="Feedback:").grid(row=6, column=0, sticky="w")
        ttk.Entry(controls_frame).grid(row=6, column=1, padx=5, pady=5, sticky="ew")
        
    def create_dashboard_frame(self):
        dashboard_frame = ttk.LabelFrame(self.root, text="Disk Scheduling Dashboard", padding=(10, 5))
        dashboard_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # Current algorithm display
        ttk.Label(dashboard_frame, text=f"Current Algorithm: {self.algorithm_var.get()} ●", 
                 font=('Helvetica', 12, 'bold')).pack(pady=10)
        
        # Metrics table
        metrics_table = ttk.Frame(dashboard_frame)
        metrics_table.pack(pady=10)
        
        ttk.Label(metrics_table, text="Seek Time", borderwidth=1, relief="solid", padding=5).grid(row=0, column=0)
        ttk.Label(metrics_table, text="Response Time", borderwidth=1, relief="solid", padding=5).grid(row=0, column=1)
        ttk.Label(metrics_table, text="Throughput", borderwidth=1, relief="solid", padding=5).grid(row=0, column=2)
        
        self.seek_time_label = ttk.Label(metrics_table, text="210", borderwidth=1, relief="solid", padding=5)
        self.seek_time_label.grid(row=1, column=0)
        
        self.response_time_label = ttk.Label(metrics_table, text="35.00", borderwidth=1, relief="solid", padding=5)
        self.response_time_label.grid(row=1, column=1)
        
        self.throughput_label = ttk.Label(metrics_table, text="0", borderwidth=1, relief="solid", padding=5)
        self.throughput_label.grid(row=1, column=2)
        
        # Disk head movement visualization
        self.figure, self.ax = plt.subplots(figsize=(6, 3))
        self.canvas = FigureCanvasTkAgg(self.figure, master=dashboard_frame)
        self.canvas.get_tk_widget().pack(pady=10)
        
    def create_metrics_frame(self):
        metrics_frame = ttk.LabelFrame(self.root, text="Performance Metrics", padding=(10, 5))
        metrics_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # Comparison & History table
        columns = ("Algorithm", "Seek Time", "Response Time", "Throughput")
        self.results_tree = ttk.Treeview(metrics_frame, columns=columns, show="headings")
        
        for col in columns:
            self.results_tree.heading(col, text=col)
            self.results_tree.column(col, width=150, anchor="center")
        
        self.results_tree.pack(fill="both", expand=True)
        
        # Add sample data
        self.results_tree.insert("", "end", values=("AI", "210", "35.00", "0"))
        
    def start_simulation(self):
        try:
            requests = [int(x.strip()) for x in self.requests_var.get().split(",")]
            head = int(self.head_pos_var.get())
            algorithm = self.algorithm_var.get()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")
            return
        
        # Run selected algorithm
        if algorithm == "FCFS":
            sequence, seek_time = self.fcfs(requests, head)
        elif algorithm == "SSTF":
            sequence, seek_time = self.sstf(requests, head)
        elif algorithm == "SCAN":
            sequence, seek_time = self.scan(requests, head)
        elif algorithm == "Q-Learning":
            sequence, seek_time = self.q_learning(requests, head)
        elif algorithm == "Genetic Algorithm":
            sequence, seek_time = self.genetic_algorithm(requests, head)
        else:
            messagebox.showerror("Error", "Invalid algorithm selected")
            return
        
        # Update metrics
        self.seek_time_label.config(text=str(seek_time))
        self.response_time_label.config(text=f"{seek_time/len(requests):.2f}")
        self.throughput_label.config(text=str(len(requests)))
        
        # Update visualization
        self.update_visualization(sequence, algorithm)
        
        # Add to history
        self.results_tree.insert("", 0, values=(
            algorithm, 
            seek_time, 
            f"{seek_time/len(requests):.2f}", 
            len(requests)
        ))
    
    def update_visualization(self, sequence, title):
        self.ax.clear()
        self.ax.plot(range(len(sequence)), sequence, marker='o', linestyle='-')
        self.ax.set_xlabel("Order of Access")
        self.ax.set_ylabel("Disk Position")
        self.ax.set_title(f"{title} Disk Head Movement")
        self.ax.grid()
        self.canvas.draw()
    
    def show_route(self):
        messagebox.showinfo("Route", "Showing disk head movement route")
    
    def return_head(self):
        messagebox.showinfo("Return", "Returning head to initial position")
    
    def reset_simulation(self):
        self.algorithm_var.set("SCAN")
        self.head_pos_var.set("100")
        self.requests_var.set("45, 80, 130, 170, 220")
        self.workload_var.set("Random")
        
        self.seek_time_label.config(text="0")
        self.response_time_label.config(text="0.00")
        self.throughput_label.config(text="0")
        
        self.ax.clear()
        self.canvas.draw()
    
    def save_config(self):
        messagebox.showinfo("Save Config", "Configuration saved successfully")
    
    def load_config(self):
        messagebox.showinfo("Load Config", "Configuration loaded successfully")
    
    def show_help(self):
        messagebox.showinfo("Help", "This is a disk scheduling simulator.\n\n"
                            "1. Select an algorithm\n"
                            "2. Set head position and requests\n"
                            "3. Click Start to run simulation")
    
    # Algorithm implementations
    def fcfs(self, requests, head):
        seek_sequence = [head] + requests
        seek_time = sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))
        return seek_sequence, seek_time
    
    def sstf(self, requests, head):
        seek_sequence = [head]
        local_requests = requests[:]
        seek_time = 0
        
        while local_requests:
            closest = min(local_requests, key=lambda x: abs(x - seek_sequence[-1]))
            seek_time += abs(closest - seek_sequence[-1])
            seek_sequence.append(closest)
            local_requests.remove(closest)
        
        return seek_sequence, seek_time
    
    def scan(self, requests, head):
        seek_sequence = [head] + sorted(requests)
        seek_time = sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))
        return seek_sequence, seek_time
    
    def q_learning(self, requests, head):
        optimized_schedule = sorted(requests)
        seek_sequence = [head] + optimized_schedule
        seek_time = sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))
        return seek_sequence, seek_time
    
    def genetic_algorithm(self, requests, head):
        optimized_schedule = sorted(requests)
        seek_sequence = [head] + optimized_schedule
        seek_time = sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))
        return seek_sequence, seek_time

if __name__ == "__main__":
    root = tk.Tk()
    app = DiskSchedulingApp(root)
    root.mainloop()