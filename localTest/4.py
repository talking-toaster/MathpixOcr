import latex2mathml.converter as converter

l = "\\begin{array}{c}\nP_{t 13} =\\pi_{f} P_{t 2} \\\\\nT_{t 13} = T_{t 2} \\pi_{f} ^ {\\frac{\\gamma-1}{\\gamma e_{f}}} \\\\\nP_{t 16} = P_{t 13} \\\\\nT_{t 16} = T_{t 13} \\\\\nP_{t 2.5} =\\pi_{C L} P_{t 2} \\\\\nT_{t 2.5} = T_{t 2} \\pi_{T L} \\frac{\\gamma-1}{\\gamma e c L} \\\\\nP_{t 3} =\\pi_{C L} P_{t 2.5} \\\\\nT_{t 3} = T_{t 2} \\pi_{\\mathrm{cH}} \\frac{\\gamma-c}{\\gamma e c L}\n\\end{array}"

print(converter.convert(l))
