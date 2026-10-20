// Valor de la UF del dia, para el estimador del sitio.
//
// mindicador.cl no permite consultas desde el navegador (CORS), asi que el
// sitio le pregunta a esta funcion y Vercel guarda la respuesta medio dia en
// su borde: una consulta real al dia, no una por visita.
module.exports = async function (req, res) {
  try {
    const r = await fetch('https://mindicador.cl/api/uf', {
      headers: { 'User-Agent': 'coryndev.com (estimador)' },
    });
    if (!r.ok) throw new Error('mindicador ' + r.status);
    const d = await r.json();
    const s = d && d.serie && d.serie[0];
    if (!s || !s.valor) throw new Error('sin serie');
    res.setHeader('Cache-Control', 'public, s-maxage=43200, stale-while-revalidate=86400');
    res.status(200).json({ valor: s.valor, fecha: s.fecha });
  } catch (e) {
    // Sin valor, el estimador muestra solo la cifra en UF: no inventa pesos.
    res.setHeader('Cache-Control', 'no-store');
    res.status(502).json({ error: 'uf no disponible' });
  }
};
