
import { GoogleGenAI, Type } from "@google/genai";
import { OptimizedRouteResponse } from "../types";

const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });

const routeSchema = {
  type: Type.OBJECT,
  properties: {
    summary: {
      type: Type.OBJECT,
      description: "Um resumo de toda a rota.",
      properties: {
        totalStops: {
          type: Type.INTEGER,
          description: "O número total de paradas para entrega.",
        },
        totalTime: {
          type: Type.STRING,
          description: "O tempo total estimado para toda a rota (ex: '2 horas 15 min').",
        },
      },
      required: ["totalStops", "totalTime"],
    },
    route: {
      type: Type.ARRAY,
      description: "O array de paradas otimizadas.",
      items: {
        type: Type.OBJECT,
        properties: {
          order: {
            type: Type.INTEGER,
            description: "A ordem sequencial da parada na rota otimizada, começando em 1.",
          },
          address: {
            type: Type.STRING,
            description: "O endereço original para esta parada.",
          },
          justification: {
            type: Type.STRING,
            description: "Uma breve explicação para posicionar esta parada nesta posição na rota (ex: 'Mais próximo da parada anterior').",
          },
          estimatedTime: {
            type: Type.STRING,
            description: "Tempo de viagem estimado da parada anterior para esta (ex: '10 min').",
          },
        },
        required: ["order", "address", "justification", "estimatedTime"],
      },
    }
  },
  required: ["summary", "route"],
};

export const optimizeRoute = async (addresses: string, startPoint?: string): Promise<OptimizedRouteResponse> => {
  const startLocation = startPoint && startPoint.trim() !== '' 
    ? `o seguinte endereço: ${startPoint}` 
    : 'um depósito central';

  const prompt = `
    Você é um especialista em logística especializado na otimização de rotas de entrega para um serviço chamado 'Sabor Express'.
    Sua tarefa é criar a rota de entrega mais eficiente para um motorista.
    Assuma que o motorista parte de ${startLocation} e deve visitar todos os endereços fornecidos.
    
    Aqui está a lista de endereços para entrega, com cada endereço em uma nova linha:
    ${addresses}

    Por favor, forneça a rota otimizada em formato JSON. A resposta deve ser um objeto JSON com duas chaves: "summary" e "route".
    - O objeto "summary" deve conter "totalStops" (a contagem dos endereços de entrega) e "totalTime" (uma string com o tempo total estimado para toda a rota).
    - O array "route" deve conter as paradas, ordenadas para máxima eficiência para economizar tempo e combustível.
    Para cada parada, inclua o endereço original, uma breve justificativa para sua posição na rota e o tempo de viagem estimado a partir da parada anterior.
  `;

  try {
    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: prompt,
      config: {
        responseMimeType: "application/json",
        responseSchema: routeSchema,
      },
    });

    const jsonText = response.text.trim();
    const routeData: OptimizedRouteResponse = JSON.parse(jsonText);
    
    // Garante que a rota está ordenada, para o caso da IA não seguir à risca
    if(routeData.route) {
        routeData.route.sort((a, b) => a.order - b.order);
    }

    return routeData;
  } catch (error) {
    console.error("Erro ao otimizar a rota com a API Gemini:", error);
    throw new Error("Falha ao gerar a rota otimizada. Por favor, verifique os endereços e tente novamente.");
  }
};