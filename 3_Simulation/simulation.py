"""
3_Simulation: Monte Carlo Simulation
This animation demonstrates a simulation process with particles.
"""

from manim import *

class SimulationAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Simulation: Particle System", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create boundary
        boundary = Rectangle(height=5, width=10, color=WHITE)
        self.play(Create(boundary))
        self.wait(0.5)
        
        # Create particles
        particles = VGroup()
        num_particles = 30
        
        for i in range(num_particles):
            particle = Dot(
                color=random.choice([RED, BLUE, GREEN, YELLOW, PURPLE]),
                radius=0.1
            )
            particle.move_to([
                np.random.uniform(-4.5, 4.5),
                np.random.uniform(-2, 2),
                0
            ])
            particles.add(particle)
        
        self.play(LaggedStart(*[FadeIn(p) for p in particles], lag_ratio=0.05))
        self.wait(0.5)
        
        # Animate particles with random movement
        animations = []
        for particle in particles:
            new_pos = [
                np.random.uniform(-4.5, 4.5),
                np.random.uniform(-2, 2),
                0
            ]
            animations.append(particle.animate.move_to(new_pos))
        
        self.play(*animations, run_time=2)
        
        # Cluster particles
        self.play(*[p.animate.move_to(ORIGIN + np.random.randn(3) * 0.5) for p in particles], run_time=1.5)
        
        # Statistics
        stats = Text("Simulation Complete\nParticles: 30\nTime: 3.5s", font_size=28, color=GREEN)
        stats.to_edge(DOWN)
        self.play(Write(stats))
        
        self.wait(2)


if __name__ == "__main__":
    import os
    os.system("manim -pqh --format=mp4 --media_dir ./media 3_Simulation/simulation.py SimulationAnimation")
