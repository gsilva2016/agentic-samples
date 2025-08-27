# POS Multimodal AI Agent
<img width="2387" height="906" alt="pos_multimodal_agent" src="https://github.com/user-attachments/assets/7612ba6d-ec97-4a46-8aa3-d0257c6c5d20" />
Demonstrates a multimodal AI agent for improving operational efficiency of POS stations. This sample provides two tools, which will upon called by the AI Agent, return POS data and AI recognition co-companion system data results.  
The POS tool returns data to simulate items which were barcode scanned or weighed. The AI recognition co-companion system tool is to simulate the object detection and classification event driven state 
which tracks total unique items it recognizes from attached cameras over a POS station. Both tools are randomized to simulate different scenarios such as:

Use Case #1
- POS tracked one bottle scanned
- AI co-companion system recognized one bottle from customer
- Result: All items handled correctly at POS / no discrepancies reported

Use Case #2
- POS tracked one bottle scanned and one bannana weighed
- AI co-companion system recognized one bottle only
- Result: Discrepancy detected between the two tools is reported along with a detailed analysis

The multimodal AI Agent uses these two tools to discover POS discrepancies such as missed-scans. Future work / considerations are to discover and report missed scans associated with unique employee personnel and beyond. 
Such future opportunities include reporting POS being unattended real-time or reported across hours, days, etc. The report generation action is TBD (e.g. a tool or another agent could handle these future features)


## Installation
Get started by running the below command.

```
./install.sh
```

Note: if this script has already been performed and you'd like to re-install the sample project only then the below command can be used to skip the re-install of dependencies.

```
./install.sh --skip
```

## Run Examples

### Run vLLM
Be sure to set your HF_TOKEN in the .env file before running the below.

```
./run-vllm.sh
```

### Run ADK Web Demo
After running the below command launch a browser to 127.0.0.1:8000 and select "pos_agent_adk_web" and enable "Token Streaming" from the UI to get started.
```
./src/run-adkweb.sh
```
