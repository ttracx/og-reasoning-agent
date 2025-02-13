import sympy as sp

class ComputationAgent:
    def calculate(self, question, context):
        if "mud weight" in question.lower():
            return self.calculate_mud_weight(context)
        return "No computation needed."

    def calculate_mud_weight(self, context):
        # Example: Mud Weight (MW) = Pore Pressure (PP) / (0.052 × Depth)
        depth = 12000  # Example depth in ft
        pore_pressure = 0.48  # Example pore pressure in psi/ft
        MW = pore_pressure / (0.052 * depth)
        return f"Recommended Mud Weight: {MW:.2f} ppg"
