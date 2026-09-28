from app.graph.workflow import deviation_graph


sample_text = """
On 26 September 2026, during manufacturing of Paracetamol API
batch B240901, the reactor temperature exceeded the approved
operating range of 80-85°C.

The temperature reached 91°C and remained above the approved
limit for approximately 18 minutes.

The event was detected by the production operator during routine
monitoring. The batch was immediately placed on hold and the
reactor temperature was restored to the approved range.

QA was informed and an investigation was initiated.
"""


result = deviation_graph.invoke({
    "raw_text": sample_text
})


print("\n================ AI EXTRACTION ================\n")

for key, value in result["extracted_data"].items():
    print(f"{key}: {value}")

print("\n================================================")