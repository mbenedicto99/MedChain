# MedChain
Desing blockchain for healthcare, healthcoin and cryptomed.

A proposta envolve a troca de informações por meios públicos utilizando o blockchain como um gerenciador de controle de acesso e validando informações externas aos blocos. Atualmente não existem padrões abertos ou implementações de blockchain que utilizam essa abordagem, mas a pesquisa apoia a viabilidade da solução proposta.

Bitcoin já demonstrou que a computação confiável e auditável é possível usando uma rede distribuída acompanhada por um ledger compartilhado. Além disso, as tecnologias para armazenamento de dados, segurança e criptografia existem e estão em uso hoje. Este artigo toma emprestado pesadamente da pesquisa publicada do Massachusetts Institute of Technology sobre o uso de uma cadeia de bloqueios pública para gerenciar e controlar o acesso a dados pessoais.

Quando um responsável medico cria um registro (prescrição, teste de laboratório, resultado de patologia, ressonância magnética), uma assinatura digital seria criada para verificar a autenticidade do documento ou imagem. Os dados seriam criptografados e enviados para o datalake para armazenamento. Toda vez que as informações são salvas no datalake, um ponteiro para o registro de saúde é criado no bloco junto com o identificador exclusivo do usuário. O doente é notificado de que os dados médicos foram adicionados ao seu blockchain. Da mesma forma um paciente seria capaz de adicionar dados de saúde com assinaturas digitais e criptografia de aplicações móveis e sensores wearable.
