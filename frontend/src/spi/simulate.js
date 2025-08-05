export async function simulateRequest(payload) {
    const response = await fetch("https://mirrormlm.onrender.com/api/simulate", {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    if (!response.ok) {
        const error = await response.text();
        throw new Error(`API Error: ${response.status} - ${error}`);
    }

    const data = await response.json();
    return data;
}
