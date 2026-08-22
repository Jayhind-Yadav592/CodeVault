import os

with open('frontend/src/pages/ProjectDetail.tsx', 'r') as f:
    c = f.read()

tabs = """      <div className="flex gap-4 border-b">
        <div className="px-4 py-2 border-b-2 border-blue-600 text-blue-600 font-medium">Overview</div>
        <div className="px-4 py-2 text-gray-900 cursor-not-allowed">Repository</div>
        <div className="px-4 py-2 text-gray-900 cursor-not-allowed">Team</div>
        <div className="px-4 py-2 text-gray-900 cursor-not-allowed">Settings</div>
      </div>"""

new_tabs = """      <div className="flex gap-4 border-b">
        <button onClick={() => setTab('overview')} className={`px-4 py-2 font-medium ${tab === 'overview' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-slate-600 hover:text-slate-900'}`}>Overview</button>
        <button onClick={() => setTab('repository')} className={`px-4 py-2 font-medium ${tab === 'repository' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-slate-600 hover:text-slate-900'}`}>Repository</button>
        <button onClick={() => setTab('team')} className={`px-4 py-2 font-medium ${tab === 'team' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-slate-600 hover:text-slate-900'}`}>Team</button>
        <button onClick={() => setTab('settings')} className={`px-4 py-2 font-medium ${tab === 'settings' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-slate-600 hover:text-slate-900'}`}>Settings</button>
      </div>"""

if tabs in c:
    c = c.replace(tabs, new_tabs)
    c = c.replace('const [loading, setLoading] = useState(true);', "const [loading, setLoading] = useState(true);\n  const [tab, setTab] = useState('overview');")
    
    body = """      <div className="grid grid-cols-3 gap-6 mt-6">
        <div className="col-span-2 space-y-6">"""
    
    new_body = """      {tab === 'overview' && (
      <div className="grid grid-cols-3 gap-6 mt-6">
        <div className="col-span-2 space-y-6">"""
    
    c = c.replace(body, new_body)
    
    c = c.replace("""        </div>
      </div>
    </div>
  );
};""", """        </div>
      </div>
      )}
      {tab !== 'overview' && (
        <div className="py-12 flex flex-col items-center justify-center bg-white rounded-[18px] border border-slate-200 mt-6 shadow-sm">
          <h3 className="text-lg font-semibold text-slate-800">No Data Available</h3>
          <p className="text-slate-500 mt-2">This section has no records or configuration yet.</p>
        </div>
      )}
    </div>
  );
};""")
    
    with open('frontend/src/pages/ProjectDetail.tsx', 'w') as f:
        f.write(c)
    print("SUCCESS")
else:
    print("FAILED TO MATCH")
